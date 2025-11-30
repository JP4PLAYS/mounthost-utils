from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parent
THEME_COMP = ROOT / "src" / "lib" / "components" / "MountHeroCtas.svelte"


def copy_component() -> None:
    dst = ROOT / "src" / "lib" / "components" / "MountHeroCtas.svelte"
    dst.parent.mkdir(parents=True, exist_ok=True)
    data = THEME_COMP.read_text(encoding="utf-8")
    if dst.exists():
        backup = dst.with_suffix(dst.suffix + ".bak")
        dst.replace(backup)
        print(f"[backup] {dst} -> {backup}")
    dst.write_text(data, encoding="utf-8")
    print(f"[copiado] MountHeroCtas.svelte -> {dst}")


def patch_page_svelte() -> None:
    page_file = ROOT / "src" / "routes" / "+page.svelte"
    if not page_file.exists():
        print("[erro] src/routes/+page.svelte não encontrado.")
        return

    text = page_file.read_text(encoding="utf-8")

    if "MountHeroCtas" in text:
        print("[ok] +page.svelte já usa MountHeroCtas, nada a fazer.")
        return

    # Adiciona import antes de </script>
    if "</script>" in text:
        before, after = text.split("</script>", 1)
        if "MountHeroCtas" not in before:
            before += "\nimport MountHeroCtas from '$lib/components/MountHeroCtas.svelte';\n"
        text = before + "</script>" + after
        print("[ok] Import MountHeroCtas adicionado.")
    else:
        print("[aviso] Não há <script> em +page.svelte; adicione manualmente o import.")

    # Insere componente abaixo do parágrafo principal do hero
    hero_snippet = "Coleção de ferramentas gratuitas da MountHost para criar, configurar e otimizar servidores de Minecraft de forma simples e rápida."
    marker = hero_snippet + "</p>"
    if marker in text and "<MountHeroCtas" not in text:
        text = text.replace(marker, marker + "\n\n  <MountHeroCtas />")
        print("[ok] <MountHeroCtas /> inserido abaixo do texto principal.")
    elif "<MountHeroCtas" not in text:
        print("[aviso] Não consegui localizar o parágrafo do hero; insira <MountHeroCtas /> manualmente onde desejar.")

    page_file.write_text(text, encoding="utf-8")
    print("[ok] src/routes/+page.svelte atualizado.")


def main() -> None:
    copy_component()
    patch_page_svelte()
    print("\nConcluído! Rode `npm run dev` e confira os botões na home.")


if __name__ == "__main__":
    main()
