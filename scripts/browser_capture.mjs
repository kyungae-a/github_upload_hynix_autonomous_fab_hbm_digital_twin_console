import { createRequire } from "module";
import path from "path";

const require = createRequire(import.meta.url);
const [browserPath, url, outPath, repoRoot] = process.argv.slice(2);

function resolvePlaywright(root) {
  const candidates = [
    path.join(root, "node_modules"),
    path.join(root, "..", "frontend", "node_modules"),
    process.env.NODE_PATH || "",
  ].filter(Boolean);
  return require(require.resolve("playwright-core", { paths: candidates }));
}

const { chromium } = resolvePlaywright(repoRoot);
const browser = await chromium.launch({
  executablePath: browserPath,
  headless: true,
  args: [
    "--disable-gpu",
    "--disable-gpu-compositing",
    "--disable-gpu-rasterization",
    "--disable-gpu-sandbox",
    "--disable-dev-shm-usage",
    "--allow-file-access-from-files",
  ],
});
const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
await page.goto(url, { waitUntil: "networkidle" });
await page.screenshot({ path: outPath, fullPage: true });
await browser.close();
console.log(JSON.stringify({ status: "PASS", url, outPath }));
