# MouseTrail Themes

<div align="center">
  <img src="assets/swatches/aurora.svg" alt="MouseTrail trail theme" width="520">
</div>

<p align="center">
  <strong>Beautiful cursor trails, one click away.</strong>
</p>

<p align="center">
  A public library of gradient trail themes for MouseTrail, the macOS
  cursor-trail app — each a plain, hand-readable JSON file describing a trail's
  color mode (<code>rainbow</code>, <code>fixed</code>, or a 2–5 stop
  <code>gradient</code>), lifetime, and width. Browse the gallery, one-click add
  a theme to the app, or download the <code>.json</code> and import it yourself.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/platform-macOS-475A60.svg" alt="Platform: macOS">
  <img src="https://img.shields.io/badge/format-plain%20JSON-216C83.svg" alt="Format: plain JSON">
  <a href="https://apps.apple.com/au/app/mousetrail/id6787651654?mt=12"><img src="https://img.shields.io/badge/App%20Store-MouseTrail-0D96F6.svg" alt="Get MouseTrail on the App Store"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC%20BY--NC%204.0-C8553D.svg" alt="License: CC BY-NC 4.0"></a>
  <a href="https://discord.com/channels/1529997922643476652/1529997923201585244"><img src="https://img.shields.io/badge/discord-community-5865F2.svg" alt="Discord community"></a>
</p>

<p align="center">
  <a href="https://timetxt.github.io/mousetrail-themes/">Gallery</a> ·
  <a href="#using-a-theme">Using a Theme</a> ·
  <a href="#collections">Collections</a> ·
  <a href="THEME-FORMAT.md">Theme Format</a> ·
  <a href="CONTRIBUTING.md">Contributing</a> ·
  <a href="README.zh-Hans.md">简体中文</a>
</p>

**[Browse and try every theme live in the gallery](https://timetxt.github.io/mousetrail-themes/)** —
click any color board and move your pointer to feel that theme drawn as a real cursor
trail, adjust its length and width, then **Add to MouseTrail** in one click or
**[get the app on the App Store](https://apps.apple.com/au/app/mousetrail/id6787651654?mt=12)**.

> 🐍 **New in the app:** MouseTrail now has a **Snake Game** — turn your trail into
> a snake, steer it with your mouse, and chase your all-time high score. Free, in
> [the latest version](https://apps.apple.com/au/app/mousetrail/id6787651654?mt=12).

## Using a theme

**1. Gallery "Add to MouseTrail" (recommended)**

Open the [gallery site](https://timetxt.github.io/mousetrail-themes/) (`docs/index.html`,
published via GitHub Pages) and click **Add to MouseTrail** on any theme card. This opens a `mousetrail://import?url=...` deep link that
hands the theme's raw JSON URL to the app, which downloads it, shows a confirmation
dialog listing the theme name(s), and only imports on your confirmation — nothing is
applied silently.

This requires a version of MouseTrail with gradient-theme support. If you're on an older
version, importing a theme with a `gradient` color mode shows an **"update MouseTrail"**
message instead of failing silently or importing incorrectly — themes with only
`rainbow`/`fixed` color modes still import fine on older versions.

**2. Download + manual import**

Click **Download .json** on a theme card (or grab any file directly from `themes/`),
then in MouseTrail go to **Settings → Trail → Import…** and choose the file. This works
on every MouseTrail version — you'll just see the same "update MouseTrail" message on
gradient themes if your app predates gradient support.

## Collections

### Designer (flagship)

Curated, sophisticated multi-stop palettes in `themes/official/designer/` — muted,
cohesive color stories rather than raw RGB picks.

| Swatch | Name | Colors |
|---|---|---|
| ![Algae Milk Cocoa trail swatch](assets/swatches/algae-milk-cocoa.svg) | Algae Milk Cocoa | `#C7D3DB` → `#A79A8A` → `#FCF7DF` → `#3E3630` |
| ![Almond Milk trail swatch](assets/swatches/almond-milk.svg) | Almond Milk | `#696C75` → `#E3CDBA` → `#F9F8F9` |
| ![Apricot Silk trail swatch](assets/swatches/apricot-silk.svg) | Apricot Silk | `#F2B382` → `#F8D0B0` → `#FBE3D2` → `#FFF8DD` |
| ![Ash Blush trail swatch](assets/swatches/ash-blush.svg) | Ash Blush | `#5E6566` → `#959BA9` → `#E1C6C0` |
| ![Ash Lilac trail swatch](assets/swatches/ash-lilac.svg) | Ash Lilac | `#363636` → `#B0A4E3` |
| ![Berry Parfait trail swatch](assets/swatches/berry-parfait.svg) | Berry Parfait | `#BF2B5C` → `#B37BC6` → `#EF95B1` → `#BEACCC` |
| ![Berry Whisper Breeze trail swatch](assets/swatches/berry-whisper-breeze.svg) | Berry Whisper Breeze | `#FFD3D4` → `#D5EBE4` → `#F8F4E8` → `#775C56` |
| ![Caramel Latte trail swatch](assets/swatches/caramel-latte.svg) | Caramel Latte | `#8D6E63` → `#D7CCC8` → `#F5F5F5` |
| ![Carnation Court trail swatch](assets/swatches/carnation-court.svg) | Carnation Court | `#F9F2E0` → `#FDAAC0` → `#003731` |
| ![Chapter Sixty-Five trail swatch](assets/swatches/chapter-sixty-five.svg) | Chapter Sixty-Five | `#A67E4B` → `#AB2719` → `#DDD6CE` → `#17252F` → `#602822` |
| ![Citron Stone trail swatch](assets/swatches/citron-stone.svg) | Citron Stone | `#696C75` → `#E7E5CD` → `#E7D558` |
| ![Clay Rose trail swatch](assets/swatches/clay-rose.svg) | Clay Rose | `#C27B7B` → `#EEAAAA` → `#F6D6D6` → `#FDEEEE` |
| ![Cloud Indigo trail swatch](assets/swatches/cloud-indigo.svg) | Cloud Indigo | `#3949AB` → `#7986CB` → `#ECEFF1` |
| ![Coral Drift trail swatch](assets/swatches/coral-drift.svg) | Coral Drift | `#C94840` → `#6393A6` → `#A3BCC6` → `#E3D3C9` |
| ![Cream trail swatch](assets/swatches/cream.svg) | Cream | `#C9A876` → `#E0C79A` → `#EFDDBB` → `#F7EEDA` |
| ![Cyberpunk trail swatch](assets/swatches/cyberpunk.svg) | Cyberpunk | `#2A1A4D` → `#7B2F87` → `#C24A93` → `#7B6DC4` → `#3CC0CE` |
| ![Delft Amethyst trail swatch](assets/swatches/delft-amethyst.svg) | Delft Amethyst | `#41386B` → `#7A70BA` → `#B1B4C8` → `#EBEED5` → `#B0C49C` |
| ![Denim Fade trail swatch](assets/swatches/denim-fade.svg) | Denim Fade | `#5B8FBE` → `#86A5C4` → `#C1D7EF` → `#E0EDF8` |
| ![Distant Sky Blue trail swatch](assets/swatches/distant-sky-blue.svg) | Distant Sky Blue | `#D0DFE6` → `#C3D7DF` → `#BACCD9` |
| ![Dopamine Harvest trail swatch](assets/swatches/dopamine-harvest.svg) | Dopamine Harvest | `#DCD7D5` → `#FAB449` → `#61911C` → `#2B3C56` → `#633D13` |
| ![Dusk Corsage trail swatch](assets/swatches/dusk-corsage.svg) | Dusk Corsage | `#DBC4DE` → `#FCE9EA` → `#5960A4` |
| ![Elderberry trail swatch](assets/swatches/elderberry.svg) | Elderberry | `#AD2B79` → `#BF5CA1` → `#CE9FBB` → `#EFBB95` |
| ![Ember Dusk trail swatch](assets/swatches/ember-dusk.svg) | Ember Dusk | `#243146` → `#D97556` → `#F1AD5F` |
| ![Enamel Blue trail swatch](assets/swatches/enamel-blue.svg) | Enamel Blue | `#15559A` → `#F7DE98` → `#144A74` |
| ![Fjord Marble trail swatch](assets/swatches/fjord-marble.svg) | Fjord Marble | `#002A3D` → `#2F506C` → `#577DA4` → `#739CC7` → `#A1BCD5` |
| ![Forest Ember trail swatch](assets/swatches/forest-ember.svg) | Forest Ember | `#872408` → `#E2782F` → `#F7D475` → `#403314` → `#4A230E` |
| ![Forest Mist trail swatch](assets/swatches/forest-mist.svg) | Forest Mist | `#4B7043` → `#B7BF8E` → `#E7E5CD` |
| ![Frost Blue trail swatch](assets/swatches/frost-blue.svg) | Frost Blue | `#8CC6ED` → `#C0E0F8` → `#D0E8FF` → `#EDF7FF` |
| ![Gaudi Arcade trail swatch](assets/swatches/gaudi-arcade.svg) | Gaudi Arcade | `#CDC8B8` → `#DEA044` → `#BF8250` → `#9D473A` → `#416A81` |
| ![Gem Blue trail swatch](assets/swatches/gem-blue.svg) | Gem Blue | `#2486B9` → `#1781B5` → `#1177B0` |
| ![Glacial Lake trail swatch](assets/swatches/glacial-lake.svg) | Glacial Lake | `#1E314A` → `#7F8A96` → `#A7C8E8` → `#C8D2DB` → `#F6FAFF` |
| ![Glaze Indigo trail swatch](assets/swatches/glaze-indigo.svg) | Glaze Indigo | `#126BAE` → `#1661AB` → `#0F59A4` |
| ![Grape Cream trail swatch](assets/swatches/grape-cream.svg) | Grape Cream | `#E23B7B` → `#CC6EC3` → `#EAA0B1` → `#FFD7F3` |
| ![Harbor Mist trail swatch](assets/swatches/harbor-mist.svg) | Harbor Mist | `#5A97D0` → `#79B0D7` → `#A0C8E8` → `#C6E0F2` |
| ![Harvest Slate trail swatch](assets/swatches/harvest-slate.svg) | Harvest Slate | `#3E5770` → `#F1AD5F` → `#D3D2BF` |
| ![Hibiscus Ice trail swatch](assets/swatches/hibiscus-ice.svg) | Hibiscus Ice | `#A55E91` → `#D0B8C4` → `#BDF3F9` |
| ![Indigo Garden trail swatch](assets/swatches/indigo-garden.svg) | Indigo Garden | `#5960A4` → `#A6D3A2` → `#C7CDE8` |
| ![Indigo Mint trail swatch](assets/swatches/indigo-mint.svg) | Indigo Mint | `#7A77B0` → `#5960A4` → `#A4D6C1` |
| ![Jasmine Light Tea trail swatch](assets/swatches/jasmine-light-tea.svg) | Jasmine Light Tea | `#F4F8F4` → `#DCE8DC` → `#C4D8C4` → `#8AA88A` |
| ![Kiln Blush trail swatch](assets/swatches/kiln-blush.svg) | Kiln Blush | `#3E5770` → `#D97556` → `#E1C6C0` |
| ![Kingfisher trail swatch](assets/swatches/kingfisher.svg) | Kingfisher | `#0095D9` → `#F6CB1D` |
| ![Lagoon Peach trail swatch](assets/swatches/lagoon-peach.svg) | Lagoon Peach | `#6398A9` → `#96C7B3` → `#F9B95C` |
| ![Lavender Nightfall trail swatch](assets/swatches/lavender-nightfall.svg) | Lavender Nightfall | `#C7CDE8` → `#FCE9EA` → `#5960A4` |
| ![Lilac Tide trail swatch](assets/swatches/lilac-tide.svg) | Lilac Tide | `#B0AFD7` → `#DBC4DE` → `#024D62` |
| ![Mandarin Linen trail swatch](assets/swatches/mandarin-linen.svg) | Mandarin Linen | `#6B7BB4` → `#89A411` → `#F58E3C` → `#FDEBD3` |
| ![Maple Sumac trail swatch](assets/swatches/maple-sumac.svg) | Maple Sumac | `#FEBA52` → `#E7993A` → `#923C27` → `#632223` → `#8D2831` |
| ![Matcha trail swatch](assets/swatches/matcha.svg) | Matcha | `#6B7A3A` → `#8A9A54` → `#A8B778` → `#CBD3A6` → `#EDE9D2` |
| ![Meadow Tide trail swatch](assets/swatches/meadow-tide.svg) | Meadow Tide | `#90BFCF` → `#AFD1BF` → `#CFE5BB` → `#E0EEB8` |
| ![Misty Blush trail swatch](assets/swatches/misty-blush.svg) | Misty Blush | `#FF6F61` → `#F8BBD0` → `#FFF8E1` |
| ![Monsoon Hush trail swatch](assets/swatches/monsoon-hush.svg) | Monsoon Hush | `#182933` → `#304753` → `#384E4C` → `#7999A4` → `#BCD0D5` |
| ![Morandi trail swatch](assets/swatches/morandi.svg) | Morandi | `#7E8A82` → `#94918E` → `#A99E9A` → `#B3A8AE` → `#C7C4BE` |
| ![Mulberry Mist trail swatch](assets/swatches/mulberry-mist.svg) | Mulberry Mist | `#835AAF` → `#A88DE2` → `#DBCCFF` → `#DEE6EE` |
| ![Olive Grove trail swatch](assets/swatches/olive-grove.svg) | Olive Grove | `#8CB26C` → `#AAC576` → `#D7E9BC` → `#EEF5E9` |
| ![Olive Linen trail swatch](assets/swatches/olive-linen.svg) | Olive Linen | `#696C75` → `#B7BF8E` → `#FEF5EE` |
| ![Orchard Frost trail swatch](assets/swatches/orchard-frost.svg) | Orchard Frost | `#9ABF17` → `#84BF93` → `#AED9C5` → `#DDECF1` |
| ![Orchid Whisper trail swatch](assets/swatches/orchid-whisper.svg) | Orchid Whisper | `#DBC4DE` → `#7A77B0` → `#FCE9EA` |
| ![Pale Fern trail swatch](assets/swatches/pale-fern.svg) | Pale Fern | `#95A69C` → `#E7E5CD` → `#FEF5EE` |
| ![Peach trail swatch](assets/swatches/peach.svg) | Peach | `#E68A5E` → `#F4B98E` → `#FBDDC2` |
| ![Peach Hazelnut trail swatch](assets/swatches/peach-hazelnut.svg) | Peach Hazelnut | `#78A5CE` → `#FFF0D9` → `#DDA4B4` → `#7C5549` |
| ![Perilla Plum trail swatch](assets/swatches/perilla-plum.svg) | Perilla Plum | `#824B75` → `#B26079` → `#E595D4` → `#EAD6E3` |
| ![Periwinkle Hush trail swatch](assets/swatches/periwinkle-hush.svg) | Periwinkle Hush | `#B0AFD7` → `#DBC4DE` → `#7A77B0` |
| ![Persimmon Grove trail swatch](assets/swatches/persimmon-grove.svg) | Persimmon Grove | `#62768E` → `#91C0EF` → `#F7C97F` → `#E87425` → `#571801` |
| ![Pine Frost trail swatch](assets/swatches/pine-frost.svg) | Pine Frost | `#162534` → `#214357` → `#37495B` → `#9AB6CE` → `#CCD8E8` |
| ![Pine Glade trail swatch](assets/swatches/pine-glade.svg) | Pine Glade | `#4CAF50` → `#81C784` → `#E8F5E9` |
| ![Pine Ivory trail swatch](assets/swatches/pine-ivory.svg) | Pine Ivory | `#0A3D2E` → `#FFD9D1` |
| ![Purple Cabbage trail swatch](assets/swatches/purple-cabbage.svg) | Purple Cabbage | `#977DB2` → `#BC7DAC` → `#A3AAE5` → `#B5EBF4` |
| ![Reverie trail swatch](assets/swatches/reverie.svg) | Reverie | `#B883D3` → `#C4A5DE` → `#A1A9D0` → `#96CCCB` → `#CFEAF1` |
| ![Rose Gold trail swatch](assets/swatches/rose-gold.svg) | Rose Gold | `#FF4777` → `#FBDC92` |
| ![Rose Powder trail swatch](assets/swatches/rose-powder.svg) | Rose Powder | `#F0A0A0` → `#F8C8C8` → `#FBE6E6` → `#FFF5F5` |
| ![Rose Toast trail swatch](assets/swatches/rose-toast.svg) | Rose Toast | `#D9A7B0` → `#F4E8DB` → `#EBC5C9` → `#A67C6B` → `#5A2F3A` |
| ![Sage Olive trail swatch](assets/swatches/sage-olive.svg) | Sage Olive | `#95A69C` → `#B7BF8E` → `#FEF5EE` |
| ![Sage Shore trail swatch](assets/swatches/sage-shore.svg) | Sage Shore | `#4B7043` → `#95A69C` → `#F9F8F9` |
| ![Sage Whisper trail swatch](assets/swatches/sage-whisper.svg) | Sage Whisper | `#C2E2C2` → `#CDE5CD` → `#DCE9DC` → `#E8EEDC` |
| ![Sakura trail swatch](assets/swatches/sakura.svg) | Sakura | `#E39BB4` → `#F2B8CE` → `#F9D3E1` → `#FCEDF2` |
| ![Sand Sage trail swatch](assets/swatches/sand-sage.svg) | Sand Sage | `#95A69C` → `#E3CDBA` → `#FEF5EE` |
| ![Sapphire Sprout trail swatch](assets/swatches/sapphire-sprout.svg) | Sapphire Sprout | `#053154` → `#BCE672` |
| ![Sea Sky Blue trail swatch](assets/swatches/sea-sky-blue.svg) | Sea Sky Blue | `#C6E6E8` → `#B0D5DF` → `#8ABCD1` |
| ![Sky Wash trail swatch](assets/swatches/sky-wash.svg) | Sky Wash | `#7EBCF5` → `#98C9F1` → `#B4DCEC` → `#D0ECE9` |
| ![Slate Coral trail swatch](assets/swatches/slate-coral.svg) | Slate Coral | `#243146` → `#959BA9` → `#E08C7A` |
| ![Smoked Terracotta trail swatch](assets/swatches/smoked-terracotta.svg) | Smoked Terracotta | `#984216` → `#E4D6C5` → `#78898F` → `#8D957E` |
| ![Spring Day trail swatch](assets/swatches/spring-day.svg) | Spring Day | `#FFAAA5` → `#FFD3B6` → `#DCEDC1` → `#A8E6CF` |
| ![Spring Dew trail swatch](assets/swatches/spring-dew.svg) | Spring Dew | `#B2D990` → `#B9DDCF` → `#C1E9E9` → `#E5F1E5` |
| ![Stone Tide trail swatch](assets/swatches/stone-tide.svg) | Stone Tide | `#3E5770` → `#5E6566` → `#D3D2BF` |
| ![Stream Stone Blue trail swatch](assets/swatches/stream-stone-blue.svg) | Stream Stone Blue | `#66A9C9` → `#619AC3` → `#5698C3` |
| ![Taro Cream trail swatch](assets/swatches/taro-cream.svg) | Taro Cream | `#D16598` → `#D893CF` → `#A9A7E8` → `#EBE7DD` |
| ![Teal Blossom trail swatch](assets/swatches/teal-blossom.svg) | Teal Blossom | `#024D62` → `#FCE9EA` → `#DBC4DE` |
| ![Tennis Court Bloom trail swatch](assets/swatches/tennis-court-bloom.svg) | Tennis Court Bloom | `#FFE5F4` → `#5E8D66` → `#F1A6BC` → `#022414` |
| ![Tiffany trail swatch](assets/swatches/tiffany.svg) | Tiffany | `#2E9A94` → `#57BDB5` → `#86D4CD` → `#C0E8E0` → `#EDE6D6` |
| ![Unripe Mango trail swatch](assets/swatches/unripe-mango.svg) | Unripe Mango | `#04044D` → `#102A01` → `#B59F7B` → `#C7BAA5` |
| ![Vintage Magazine trail swatch](assets/swatches/vintage-magazine.svg) | Vintage Magazine | `#D3AB78` → `#98341F` → `#DACABF` → `#E19956` → `#4A3934` |
| ![Violet Cream trail swatch](assets/swatches/violet-cream.svg) | Violet Cream | `#B377BC` → `#E8A0E3` → `#FF8A9E` → `#FFD9E4` |
| ![Windblown Wheat trail swatch](assets/swatches/windblown-wheat.svg) | Windblown Wheat | `#F7F4ED` → `#C7D3C0` → `#C8A96B` → `#8FA28A` |
| ![Windmill Meadow trail swatch](assets/swatches/windmill-meadow.svg) | Windmill Meadow | `#4A79B8` → `#E3E6EA` → `#E6D6C3` → `#687C45` → `#1E2A13` |
| ![Winter Mist trail swatch](assets/swatches/winter-mist.svg) | Winter Mist | `#021729` → `#1C405F` → `#6395BA` → `#B4D9EB` → `#DAEEF7` |
| ![Wisteria Veil trail swatch](assets/swatches/wisteria-veil.svg) | Wisteria Veil | `#897CD3` → `#9898DC` → `#B8BBE7` → `#D8DEF7` |


### Neon

Bright, saturated multi-stop gradients in `themes/official/neon/`, including the built-in
**Aurora** and **Sunset** presets that ship with the app.

| Swatch | Name | Colors |
|---|---|---|
| ![Aegean Blue trail swatch](assets/swatches/aegean-blue.svg) | Aegean Blue | `#08129C` → `#0038DE` → `#74B8FD` → `#BEF5FC` |
| ![Amber Forge trail swatch](assets/swatches/amber-forge.svg) | Amber Forge | `#252712` → `#875712` → `#FCDB56` |
| ![Aqua Surge trail swatch](assets/swatches/aqua-surge.svg) | Aqua Surge | `#06A4C0` → `#01CFD2` → `#19F0D7` → `#9FFFEC` |
| ![Aurora trail swatch](assets/swatches/aurora.svg) | Aurora | `#7B61FF` → `#00D9FF` → `#00F5A0` → `#A8FF78` |
| ![Aventurine trail swatch](assets/swatches/aventurine.svg) | Aventurine | `#0B2558` → `#1C618B` → `#2D90A7` → `#3FBFC0` → `#53F2B8` |
| ![Azure Rush trail swatch](assets/swatches/azure-rush.svg) | Azure Rush | `#0349D5` → `#3673F0` → `#39BEF9` → `#A8E6FF` |
| ![Bottle Cap trail swatch](assets/swatches/bottle-cap.svg) | Bottle Cap | `#0A31A6` → `#0A57BF` → `#7FBCF2` → `#EEDE4F` |
| ![Bougainvillea trail swatch](assets/swatches/bougainvillea.svg) | Bougainvillea | `#568BE9` → `#9390E9` → `#C36ACF` → `#EDAEC6` → `#F7EAF3` |
| ![Cabana Stripe trail swatch](assets/swatches/cabana-stripe.svg) | Cabana Stripe | `#155465` → `#3792A7` → `#F35553` → `#EFE2C8` |
| ![Candy Pop trail swatch](assets/swatches/candy-pop.svg) | Candy Pop | `#FF10AB` → `#FF4FC4` → `#FF84EA` → `#FFC0F5` |
| ![Citrus Sea trail swatch](assets/swatches/citrus-sea.svg) | Citrus Sea | `#48C6F0` → `#FFF0D6` → `#FF8A3D` |
| ![Clementine Breeze trail swatch](assets/swatches/clementine-breeze.svg) | Clementine Breeze | `#EA631B` → `#A8C2E0` → `#EBEBDF` |
| ![Crimson Pop trail swatch](assets/swatches/crimson-pop.svg) | Crimson Pop | `#D3071C` → `#F74020` → `#FF7375` → `#FFAEAF` |
| ![Dream Purple trail swatch](assets/swatches/dream-purple.svg) | Dream Purple | `#9D7CFF` → `#D291FF` → `#FFB3F7` → `#A8FFF5` |
| ![Electric Tide trail swatch](assets/swatches/electric-tide.svg) | Electric Tide | `#170E29` → `#007EFC` → `#6FE3FC` |
| ![Emerald Lagoon trail swatch](assets/swatches/emerald-lagoon.svg) | Emerald Lagoon | `#1A8B41` → `#38BCBD` → `#4EC94C` |
| ![Firecracker trail swatch](assets/swatches/firecracker.svg) | Firecracker | `#1B1512` → `#F90027` → `#2FDDCC` |
| ![Forest trail swatch](assets/swatches/forest.svg) | Forest | `#1B5E20` → `#4CAF50` → `#8BC34A` → `#CDDC39` → `#FFC107` |
| ![Galaxy trail swatch](assets/swatches/galaxy.svg) | Galaxy | `#2563EB` → `#8B5CF6` → `#EC4899` → `#F97316` → `#FDE047` |
| ![Honey Glow trail swatch](assets/swatches/honey-glow.svg) | Honey Glow | `#FFB209` → `#FFCC42` → `#FFDA77` → `#FDECBC` |
| ![Jade Current trail swatch](assets/swatches/jade-current.svg) | Jade Current | `#087471` → `#1CA041` → `#5BD8BE` |
| ![Lime Surge trail swatch](assets/swatches/lime-surge.svg) | Lime Surge | `#06B606` → `#4CD201` → `#9BF019` → `#CEFF83` |
| ![Meadowlark trail swatch](assets/swatches/meadowlark.svg) | Meadowlark | `#042C8F` → `#4891E7` → `#86D0FD` → `#BBE11A` → `#E8F957` |
| ![Mint Breeze trail swatch](assets/swatches/mint-breeze.svg) | Mint Breeze | `#A7F3D0` → `#6EE7B7` → `#38BDF8` → `#E0F2FE` |
| ![Mojave Glow trail swatch](assets/swatches/mojave-glow.svg) | Mojave Glow | `#E45F21` → `#A9BFD4` → `#E7D2BB` |
| ![Neon Iris trail swatch](assets/swatches/neon-iris.svg) | Neon Iris | `#09212C` → `#00D6DE` → `#DFB6FD` |
| ![Neon Orchid trail swatch](assets/swatches/neon-orchid.svg) | Neon Orchid | `#0D0933` → `#581B72` → `#FE00BE` |
| ![Ocean trail swatch](assets/swatches/ocean.svg) | Ocean | `#0187FF` → `#00C2FF` → `#00E9D2` → `#E0FFFA` |
| ![Periwinkle Drift trail swatch](assets/swatches/periwinkle-drift.svg) | Periwinkle Drift | `#4141BF` → `#7F8EF3` → `#9EABFF` → `#CFD7FE` |
| ![Prism Drift trail swatch](assets/swatches/prism-drift.svg) | Prism Drift | `#8E44AD` → `#4285F4` → `#1ABC9C` → `#7ACC26` |
| ![Santorini Bloom trail swatch](assets/swatches/santorini-bloom.svg) | Santorini Bloom | `#F2C400` → `#0077C8` → `#486B1F` → `#F7F4EC` |
| ![Sunset trail swatch](assets/swatches/sunset.svg) | Sunset | `#FF6B6B` → `#FFA26B` → `#FFD06B` → `#FFF7A8` |
| ![Tangerine Rush trail swatch](assets/swatches/tangerine-rush.svg) | Tangerine Rush | `#FF5100` → `#FE861D` → `#FFAD66` → `#FFCC92` |
| ![Tidewater trail swatch](assets/swatches/tidewater.svg) | Tidewater | `#3467B5` → `#5D94E6` → `#59B5F6` → `#80ECF2` → `#F2F6F7` |
| ![Ultraviolet Bloom trail swatch](assets/swatches/ultraviolet-bloom.svg) | Ultraviolet Bloom | `#5F03A8` → `#A25CFF` → `#C99AFF` → `#E0BAFF` |
| ![Verdant Pulse trail swatch](assets/swatches/verdant-pulse.svg) | Verdant Pulse | `#152C14` → `#00313F` → `#AFFDAB` |
| ![Voltage trail swatch](assets/swatches/voltage.svg) | Voltage | `#3C3C3C` → `#8000FF` → `#FF0080` → `#FFDE00` |


### Community

Contributed via pull request in `themes/community/`, reviewed by a maintainer before
merge. Previews for community themes appear in the gallery (`docs/index.html`) rather
than here.

## Hand-authoring a theme

See **[THEME-FORMAT.md](THEME-FORMAT.md)** for the full file format reference — every
field, its valid range, and worked examples (including how to convert a hex color to the
`0`–`1` sRGB values this format uses).

## Contributing

Want to add your own theme to the Community collection? See
**[CONTRIBUTING.md](CONTRIBUTING.md)** for how to author, validate, and submit a theme
via pull request.

## License

Themes and repository content in this project are licensed under
**[CC BY-NC 4.0](LICENSE)** (Attribution–NonCommercial) — free to use and share, not for
commercial use, with attribution. This license covers this repository's themes and
content only; it is independent of the MouseTrail application's own license.
