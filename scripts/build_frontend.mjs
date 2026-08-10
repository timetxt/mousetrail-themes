/**
 * The gallery is deliberately dependency-free vanilla JavaScript at this
 * revision. Keep a deterministic build gate so the GitHub Pages contract can
 * evolve to a bundled TypeScript source without changing CI commands.
 */
import { access, readFile, writeFile } from "node:fs/promises";
import { resolve } from "node:path";

const app = resolve("docs/app.js");
await access(app);
const map = resolve("docs/app.js.map");
const source = await readFile(app, "utf8");
const marker = "//# sourceMappingURL=app.js.map";
if (!source.endsWith(marker + "\n")) {
  throw new Error("docs/app.js must end with its external sourceMappingURL marker");
}
await writeFile(map, '{"version":3,"file":"app.js","sources":["app.js"],"names":[],"mappings":""}\n');
console.log("Gallery frontend is dependency-free; docs/app.js and app.js.map are ready for Pages.");
