<script lang="ts">
  const year = new Date().getFullYear();
</script>

<footer class="mt-16 border-t border-zinc-800/80 bg-black/20">
  <div class="mx-auto flex max-w-6xl flex-col gap-3 px-4 py-6 text-xs md:text-sm text-zinc-500">
    <div class="flex flex-col gap-1 md:flex-row md:items-center md:justify-between">
      <p class="text-zinc-400">
        <span class="font-semibold text-zinc-200">MountHost Utils</span>
        {" "}- coleção de utilitários gratuitos para auxiliar na criação, configuração e otimização de servidores Minecraft.
      </p>
      <p class="text-zinc-500">
        © {year} MountHost. Todos os direitos reservados.
      </p>
    </div>

    <div class="flex flex-wrap items-center gap-3 text-[11px] md:text-xs">
      <span class="uppercase tracking-wide text-zinc-500/80">Links úteis</span>
      <a
        href="https://www.mounthost.com.br/"
        target="_blank"
        rel="noreferrer"
        class="underline decoration-zinc-600 hover:decoration-blue-400"
      >
        Site oficial
      </a>
      <span class="text-zinc-700">•</span>
      <a
        href="https://discord.com/invite/dHfC5tujXx"
        target="_blank"
        rel="noreferrer"
        class="underline decoration-zinc-600 hover:decoration-blue-400"
      >
        Discord da MountHost
      </a>
      <span class="text-zinc-700">•</span>
      <a
        href="https://wa.me/556191878904"
        target="_blank"
        rel="noreferrer"
        class="underline decoration-zinc-600 hover:decoration-blue-400"
      >
        WhatsApp
      </a>
    </div>
  </div>
</footer>
