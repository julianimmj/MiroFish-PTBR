<template>
  <router-view />
</template>

<script setup>
// Gerenciamento de páginas via Vue Router
</script>

<style>
/* Reset global */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  font-family: 'Inter', 'Space Grotesk', 'Outfit', system-ui, -apple-system, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #0A0A0A;
  background-color: #ffffff;
}

/* Tipografia aprimorada */
h1, h2, h3, h4, h5, h6 {
  font-family: 'Outfit', 'Space Grotesk', system-ui, sans-serif;
  font-weight: 700;
  letter-spacing: -0.5px;
}

/* Barra de rolagem elegante */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: #f8f8f8;
}

::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg, #1a1a1a 0%, #333 100%);
  border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(180deg, #FF4500 0%, #FF6A33 100%);
}

/* Estilo global de botões */
button {
  font-family: inherit;
  transition: all 0.2s ease;
}

/* Seleção de texto elegante */
::selection {
  background: rgba(255, 69, 0, 0.15);
  color: #0A0A0A;
}

/* Links globais */
a {
  transition: all 0.2s ease;
}

/* Animações suaves globais */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes slideInRight {
  from { opacity: 0; transform: translateX(16px); }
  to { opacity: 1; transform: translateX(0); }
}
</style>
