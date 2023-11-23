<script setup lang="ts">
import { ref } from 'vue';

const text = ref('')
const showResult = ref(false)

function toggleResult() {
  showResult.value = !showResult.value
}
</script>

<template>
  <div class="bg-primary flex flex-row w-screen">
    <div :class="{ [`w-5/12`]: showResult }" class="flex flex-col gap-3 justify-center items-center h-screen w-full">
      <button type="button" v-if="showResult" class="absolute top-0 left-0 p-4" @click="toggleResult">
        <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24" fill="white">
          <path d="M400-80 0-480l400-400 71 71-329 329 329 329-71 71Z" />
        </svg>
        <span class="sr-only">Voltar</span>
      </button>

      <p class="text-white font-bold mb-6">Crie seu próprio e-commerce ✌🏻</p>

      <textarea id="message" rows="6" v-model="text" style="resize: none;"
        class="block p-2.5 w-[33vw] text-sm bg-secondary text-white text-bold marker:rounded-lg border border-accent2 rounded-xl placeholder:italic placeholder:text-lg"
        placeholder="Descreva aqui sua loja...&#10;”Quero um website para vender produtos variados, como itens para casa e eletrônicos”"></textarea>

      <button class="bg-accent w-[33vw] p-4 rounded-xl text-white" @click="toggleResult">
        {{ showResult ? "Baixar" : "Continuar" }}
      </button>
    </div>

    <div class="flex flex-col justify-center items-center h-screen w-7/12 bg-accent" v-if="showResult">
      oi
    </div>
  </div>
</template>
