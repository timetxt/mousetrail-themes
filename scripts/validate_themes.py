#!/usr/bin/env python3
"""Validate MouseTrail theme JSON files.

Pure Python stdlib only (json, pathlib, sys) -- no third-party imports, so
this script runs anywhere python3 runs, with no pip install step, and is the
single local + CI validation entry point for this repo.

Usage:
    python3 scripts/validate_themes.py              # validate themes/**/*.json
    python3 scripts/validate_themes.py --self-test   # run embedded fixtures only

Exit code 0 means every theme file validated; non-zero means at least one
violation was found (each printed as "<file>: <reason>").
"""

import json
import pathlib
import sys

# Repo root is resolved from this script's own location so the script works
# regardless of the caller's current working directory.
REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
THEMES_DIR = REPO_ROOT / "themes"

COLOR_MODE_KEYS = ("rainbow", "fixed", "gradient")


def _is_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def _is_integer(value):
    return isinstance(value, int) and not isinstance(value, bool)


def _in_unit_range(value):
    return _is_number(value) and 0 <= value <= 1


def _check_unit_field(obj, key, path, errors):
    if key not in obj:
        errors.append(f"{path}: missing required field '{key}'")
        return
    if not _in_unit_range(obj[key]):
        errors.append(
            f"{path}: field '{key}' must be a number in [0, 1], got {obj[key]!r}"
        )


def _validate_fixed(fixed, path, errors):
    if not isinstance(fixed, dict):
        errors.append(f"{path}.fixed: must be an object")
        return
    for key in ("red", "green", "blue", "alpha"):
        _check_unit_field(fixed, key, f"{path}.fixed", errors)


def _validate_gradient(gradient, path, errors):
    if not isinstance(gradient, dict):
        errors.append(f"{path}.gradient: must be an object")
        return
    stops = gradient.get("stops")
    if not isinstance(stops, list):
        errors.append(f"{path}.gradient: missing/invalid 'stops' array")
        return
    if not (2 <= len(stops) <= 5):
        errors.append(
            f"{path}.gradient: stop count {len(stops)} out of range 2-5"
        )
    for i, stop in enumerate(stops):
        stop_path = f"{path}.gradient.stops[{i}]"
        if not isinstance(stop, dict):
            errors.append(f"{stop_path}: stop must be an object")
            continue
        for key in ("red", "green", "blue", "alpha", "location"):
            _check_unit_field(stop, key, stop_path, errors)


def _validate_color_mode(color_mode, path, errors):
    """Validates a colorMode object. Returns True iff it is a valid/likely gradient mode."""
    if not isinstance(color_mode, dict):
        errors.append(f"{path}: 'colorMode' must be an object")
        return False

    present = [key for key in COLOR_MODE_KEYS if key in color_mode]
    if len(color_mode) != 1 or len(present) != 1:
        errors.append(
            f"{path}: 'colorMode' must have exactly one of "
            f"{COLOR_MODE_KEYS!r}, got keys {list(color_mode.keys())!r}"
        )

    mode = present[0] if present else None
    if mode == "rainbow":
        if not isinstance(color_mode["rainbow"], dict):
            errors.append(f"{path}.rainbow: must be an object")
        return False
    if mode == "fixed":
        _validate_fixed(color_mode["fixed"], path, errors)
        return False
    if mode == "gradient":
        _validate_gradient(color_mode["gradient"], path, errors)
        return True
    return False


def validate_document(doc, label, errors):
    """Validates one parsed theme document against `label`, appending violation
    strings to `errors`. Returns (theme_names, has_gradient) for reuse by the
    repo-wide name-uniqueness check.
    """
    names = []

    if not isinstance(doc, dict):
        errors.append(f"{label}: top-level document must be a JSON object")
        return names, False

    version = doc.get("version")
    if "version" not in doc:
        errors.append(f"{label}: missing required field 'version'")
    elif not _is_integer(version) or not (1 <= version <= 2):
        errors.append(
            f"{label}: 'version' must be an integer in [1, 2], got {version!r}"
        )

    if "themes" not in doc:
        errors.append(f"{label}: missing required field 'themes'")
        return names, False

    themes = doc["themes"]
    if not isinstance(themes, list) or len(themes) == 0:
        errors.append(f"{label}: 'themes' must be a non-empty array")
        return names, False

    has_gradient = False
    for i, theme in enumerate(themes):
        theme_path = f"{label}#themes[{i}]"
        if not isinstance(theme, dict):
            errors.append(f"{theme_path}: theme must be an object")
            continue

        name = theme.get("name")
        if not isinstance(name, str) or not name:
            errors.append(f"{theme_path}: missing/invalid 'name'")
        else:
            names.append(name)

        style = theme.get("style")
        if not isinstance(style, dict):
            errors.append(f"{theme_path}: missing/invalid 'style'")
            continue

        for key in ("lifetime", "widthScale"):
            if key not in style:
                errors.append(f"{theme_path}.style: missing required field '{key}'")
            elif not _is_number(style[key]):
                errors.append(
                    f"{theme_path}.style: field '{key}' must be a number, got {style[key]!r}"
                )

        if "colorMode" not in style:
            errors.append(f"{theme_path}.style: missing required field 'colorMode'")
        else:
            is_gradient = _validate_color_mode(
                style["colorMode"], f"{theme_path}.style", errors
            )
            has_gradient = has_gradient or is_gradient

    if _is_integer(version) and 1 <= version <= 2:
        if has_gradient and version != 2:
            errors.append(
                f"{label}: document contains a gradient theme but version is "
                f"{version} (must be 2)"
            )
        if not has_gradient and version != 1:
            errors.append(
                f"{label}: document contains no gradient theme but version is "
                f"{version} (must be 1)"
            )

    return names, has_gradient


def validate_repo(themes_dir, repo_root):
    """Validates every themes/**/*.json under `themes_dir`, including the
    repo-wide theme-name-uniqueness lint. Returns (errors, ok_files).
    """
    errors = []
    ok_files = []
    name_origin = {}

    files = sorted(themes_dir.rglob("*.json"))
    if not files:
        errors.append(
            f"{themes_dir.relative_to(repo_root)}: no theme JSON files found"
        )
        return errors, ok_files

    for file_path in files:
        label = str(file_path.relative_to(repo_root))

        # Community themes are namespaced per contributor:
        # themes/community/<github-username>/<kebab-case-name>.json.
        rel_parts = file_path.relative_to(themes_dir).parts
        if rel_parts[0] == "community" and len(rel_parts) != 3:
            errors.append(
                f"{label}: community themes must live at "
                "themes/community/<github-username>/<kebab-case-name>.json"
            )
            continue

        try:
            text = file_path.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"{label}: could not read file ({exc})")
            continue

        try:
            doc = json.loads(text)
        except json.JSONDecodeError as exc:
            errors.append(f"{label}: invalid JSON ({exc})")
            continue

        file_errors = []
        names, _ = validate_document(doc, label, file_errors)

        for name in names:
            if name in name_origin and name_origin[name] != label:
                file_errors.append(
                    f"{label}: duplicate theme name {name!r} "
                    f"(already defined in {name_origin[name]})"
                )
            else:
                name_origin.setdefault(name, label)

        if file_errors:
            errors.extend(file_errors)
        else:
            ok_files.append(label)

    return errors, ok_files


# --------------------------------------------------------------------------
# Self-test: embedded known-good and known-bad fixtures, one per failure
# class, exercised with no filesystem I/O.
# --------------------------------------------------------------------------


def _fixture_good_rainbow():
    return {
        "version": 1,
        "themes": [
            {
                "name": "Fixture Rainbow",
                "style": {
                    "colorMode": {"rainbow": {}},
                    "lifetime": 0.6,
                    "widthScale": 1.0,
                },
            }
        ],
    }


def _fixture_good_fixed():
    return {
        "version": 1,
        "themes": [
            {
                "name": "Fixture Fixed",
                "style": {
                    "colorMode": {
                        "fixed": {"red": 0.5, "green": 0.25, "blue": 0.75, "alpha": 1}
                    },
                    "lifetime": 0.6,
                    "widthScale": 1.0,
                },
            }
        ],
    }


def _fixture_good_gradient():
    return {
        "version": 2,
        "themes": [
            {
                "name": "Fixture Gradient",
                "style": {
                    "colorMode": {
                        "gradient": {
                            "stops": [
                                {"red": 0, "green": 0, "blue": 0, "alpha": 1, "location": 0},
                                {"red": 1, "green": 1, "blue": 1, "alpha": 1, "location": 1},
                            ]
                        }
                    },
                    "lifetime": 0.6,
                    "widthScale": 1.0,
                },
            }
        ],
    }


def _fixture_good_gradient_five_stops():
    stops = [
        {"red": i / 4, "green": i / 4, "blue": i / 4, "alpha": 1, "location": i / 4}
        for i in range(5)
    ]
    return {
        "version": 2,
        "themes": [
            {
                "name": "Fixture Gradient Five",
                "style": {
                    "colorMode": {"gradient": {"stops": stops}},
                    "lifetime": 0.6,
                    "widthScale": 1.0,
                },
            }
        ],
    }


def _bad_fixtures():
    """Returns a list of (label, doc) known-bad fixtures, one per failure class."""
    return [
        (
            "missing-version",
            {
                "themes": [
                    {
                        "name": "X",
                        "style": {
                            "colorMode": {"rainbow": {}},
                            "lifetime": 0.6,
                            "widthScale": 1.0,
                        },
                    }
                ]
            },
        ),
        (
            "version-out-of-range",
            {
                "version": 3,
                "themes": [
                    {
                        "name": "X",
                        "style": {
                            "colorMode": {"rainbow": {}},
                            "lifetime": 0.6,
                            "widthScale": 1.0,
                        },
                    }
                ],
            },
        ),
        (
            "version-not-integer",
            {
                "version": 1.5,
                "themes": [
                    {
                        "name": "X",
                        "style": {
                            "colorMode": {"rainbow": {}},
                            "lifetime": 0.6,
                            "widthScale": 1.0,
                        },
                    }
                ],
            },
        ),
        ("themes-empty", {"version": 1, "themes": []}),
        (
            "theme-missing-name",
            {
                "version": 1,
                "themes": [
                    {
                        "style": {
                            "colorMode": {"rainbow": {}},
                            "lifetime": 0.6,
                            "widthScale": 1.0,
                        }
                    }
                ],
            },
        ),
        (
            "theme-missing-style",
            {"version": 1, "themes": [{"name": "X"}]},
        ),
        (
            "style-missing-lifetime-widthscale",
            {
                "version": 1,
                "themes": [
                    {"name": "X", "style": {"colorMode": {"rainbow": {}}}}
                ],
            },
        ),
        (
            "colormode-two-keys",
            {
                "version": 1,
                "themes": [
                    {
                        "name": "X",
                        "style": {
                            "colorMode": {"rainbow": {}, "fixed": {
                                "red": 0, "green": 0, "blue": 0, "alpha": 1
                            }},
                            "lifetime": 0.6,
                            "widthScale": 1.0,
                        },
                    }
                ],
            },
        ),
        (
            "colormode-unknown-key",
            {
                "version": 1,
                "themes": [
                    {
                        "name": "X",
                        "style": {
                            "colorMode": {"plasma": {}},
                            "lifetime": 0.6,
                            "widthScale": 1.0,
                        },
                    }
                ],
            },
        ),
        (
            "fixed-missing-component",
            {
                "version": 1,
                "themes": [
                    {
                        "name": "X",
                        "style": {
                            "colorMode": {"fixed": {"red": 0, "green": 0, "blue": 0}},
                            "lifetime": 0.6,
                            "widthScale": 1.0,
                        },
                    }
                ],
            },
        ),
        (
            "fixed-component-out-of-range",
            {
                "version": 1,
                "themes": [
                    {
                        "name": "X",
                        "style": {
                            "colorMode": {
                                "fixed": {"red": 2.0, "green": 0, "blue": 0, "alpha": 1}
                            },
                            "lifetime": 0.6,
                            "widthScale": 1.0,
                        },
                    }
                ],
            },
        ),
        (
            "gradient-too-few-stops",
            {
                "version": 2,
                "themes": [
                    {
                        "name": "X",
                        "style": {
                            "colorMode": {
                                "gradient": {
                                    "stops": [
                                        {"red": 0, "green": 0, "blue": 0, "alpha": 1, "location": 0}
                                    ]
                                }
                            },
                            "lifetime": 0.6,
                            "widthScale": 1.0,
                        },
                    }
                ],
            },
        ),
        (
            "gradient-too-many-stops",
            {
                "version": 2,
                "themes": [
                    {
                        "name": "X",
                        "style": {
                            "colorMode": {
                                "gradient": {
                                    "stops": [
                                        {"red": i / 5, "green": 0, "blue": 0, "alpha": 1, "location": i / 5}
                                        for i in range(6)
                                    ]
                                }
                            },
                            "lifetime": 0.6,
                            "widthScale": 1.0,
                        },
                    }
                ],
            },
        ),
        (
            "gradient-stop-location-out-of-range",
            {
                "version": 2,
                "themes": [
                    {
                        "name": "X",
                        "style": {
                            "colorMode": {
                                "gradient": {
                                    "stops": [
                                        {"red": 0, "green": 0, "blue": 0, "alpha": 1, "location": -0.1},
                                        {"red": 1, "green": 1, "blue": 1, "alpha": 1, "location": 1},
                                    ]
                                }
                            },
                            "lifetime": 0.6,
                            "widthScale": 1.0,
                        },
                    }
                ],
            },
        ),
        (
            "version-mismatch-gradient-needs-2",
            {
                "version": 1,
                "themes": [
                    {
                        "name": "X",
                        "style": {
                            "colorMode": {
                                "gradient": {
                                    "stops": [
                                        {"red": 0, "green": 0, "blue": 0, "alpha": 1, "location": 0},
                                        {"red": 1, "green": 1, "blue": 1, "alpha": 1, "location": 1},
                                    ]
                                }
                            },
                            "lifetime": 0.6,
                            "widthScale": 1.0,
                        },
                    }
                ],
            },
        ),
        (
            "version-mismatch-no-gradient-needs-1",
            {
                "version": 2,
                "themes": [
                    {
                        "name": "X",
                        "style": {
                            "colorMode": {"rainbow": {}},
                            "lifetime": 0.6,
                            "widthScale": 1.0,
                        },
                    }
                ],
            },
        ),
    ]


def run_self_test():
    failures = []

    def expect_ok(label, doc):
        errors = []
        validate_document(doc, label, errors)
        if errors:
            failures.append(
                f"expected OK for good fixture {label!r} but got errors: {errors}"
            )

    def expect_fail(label, doc):
        errors = []
        validate_document(doc, label, errors)
        if not errors:
            failures.append(
                f"expected a violation for bad fixture {label!r} but validation passed"
            )

    expect_ok("good-rainbow", _fixture_good_rainbow())
    expect_ok("good-fixed", _fixture_good_fixed())
    expect_ok("good-gradient", _fixture_good_gradient())
    expect_ok("good-gradient-five-stops", _fixture_good_gradient_five_stops())

    for label, doc in _bad_fixtures():
        expect_fail(label, doc)

    # Repo-wide name-uniqueness lint, exercised without touching the filesystem.
    doc_a = _fixture_good_rainbow()
    doc_b = _fixture_good_rainbow()  # same theme name as doc_a: "Fixture Rainbow"
    origin = {}
    dup_errors = []
    for label, doc in (("dup-fixture-a.json", doc_a), ("dup-fixture-b.json", doc_b)):
        errors = []
        names, _ = validate_document(doc, label, errors)
        if errors:
            failures.append(
                f"expected OK for name-uniqueness fixture {label!r} but got errors: {errors}"
            )
        for name in names:
            if name in origin and origin[name] != label:
                dup_errors.append(
                    f"{label}: duplicate theme name {name!r} (already defined in {origin[name]})"
                )
            else:
                origin.setdefault(name, label)
    if not dup_errors:
        failures.append(
            "expected a duplicate-name violation across dup-fixture-a/b.json but none was found"
        )

    if failures:
        print(f"SELF-TEST FAIL: {len(failures)} issue(s):", file=sys.stderr)
        for f in failures:
            print(f"  {f}", file=sys.stderr)
        return 1

    total_checked = 4 + len(_bad_fixtures()) + 2
    print(f"SELF-TEST OK: {total_checked} fixture(s) behaved as expected")
    return 0


def main(argv):
    if "--self-test" in argv:
        return run_self_test()

    errors, ok_files = validate_repo(THEMES_DIR, REPO_ROOT)

    if errors:
        print(f"FAIL: {len(errors)} violation(s):", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1

    print(f"OK: {len(ok_files)} theme file(s) validated")
    for label in ok_files:
        print(f"  OK {label}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
