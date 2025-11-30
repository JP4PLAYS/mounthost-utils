from __future__ import annotations
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
THEME_ROOT = ROOT / "mounthost-theme"


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        backup = dst.with_suffix(dst.suffix + ".bak")
        shutil.copy2(dst, backup)
        print(f"[backup] {dst} -> {backup}")
    shutil.copy2(src, dst)
    print(f"[copiado] {src.relative_to(THEME_ROOT)} -> {dst.relative_to(ROOT)}")


def ensure_theme_css_link() -> None:
    app_html = ROOT / "src" / "app.html"
    if not app_html.exists():
        print("[aviso] src/app.html não encontrado; adicione manualmente o link para /mounthost-theme.css no <head>.")
        return

    text = app_html.read_text(encoding="utf-8")
    if "mounthost-theme.css" in text:
        print("[ok] Link para mounthost-theme.css já existe em src/app.html")
        return

    marker = "</head>"
    link_tag = '  <link rel="stylesheet" href="/mounthost-theme.css" />\n'
    if marker not in text:
        print("[aviso] Não encontrei </head> em src/app.html. Adicione manualmente o link para /mounthost-theme.css.")
        return

    text = text.replace(marker, link_tag + marker)
    app_html.write_text(text, encoding="utf-8")
    print("[ok] Link para mounthost-theme.css adicionado em src/app.html")


def main() -> None:
    # CSS global de tema
    src_css = THEME_ROOT / "static" / "mounthost-theme.css"
    dst_css = ROOT / "static" / "mounthost-theme.css"
    copy_file(src_css, dst_css)

    # Componentes MountHost
    components = [
        "MountTopBanner.svelte",
        "MountFooter.svelte",
        "MountSidebarBrand.svelte",
    ]
    for name in components:
        src = THEME_ROOT / "src" / "lib" / "components" / name
        dst = ROOT / "src" / "lib" / "components" / name
        copy_file(src, dst)

    ensure_theme_css_link()

    print("\nPronto!")
    print("- Execute: npm run dev")
    print("- Garanta que o layout usa <MountTopBanner />, <MountFooter /> e <MountSidebarBrand /> como você já tinha feito antes.")
    print("- O resto do site deve assumir automaticamente a paleta de cores da MountHost.")


if __name__ == "__main__":
    main()
