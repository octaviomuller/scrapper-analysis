<script setup lang="ts">
import axios from 'axios';
import { Ref, ref } from 'vue';

axios.defaults.baseURL = 'http://localhost:5000';

const text = ref('')
const isShowResult = ref(false);
const loading = ref(false)
const imageBlob: Ref<any> = ref(null);
const imageBlobUrl: Ref<any> = ref(null);

async function showResult() {
  if (!isShowResult.value) {
    loading.value = true;
    await downloadAndDisplayImage()
    loading.value = false;
    isShowResult.value = true
  } else {
    loading.value = true;
    await downloadProject()
    loading.value = false;
  }
}

function goBack() {
  isShowResult.value = false
}

const downloadProject = async () => {
  try {
    const body = {
      text: text.value
    }

    // Faça uma solicitação GET para a rota que fornece o arquivo ZIP
    const response = await axios.post('/project', body, {
      responseType: 'arraybuffer',  // Indica que a resposta deve ser tratada como um array de bytes
    });

    // Crie um objeto Blob com os dados da resposta
    const blob = new Blob([response.data], { type: 'application/zip' });

    // Crie um link para o arquivo Blob
    const link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);
    link.download = 'arquivos.zip';

    // Adicione o link ao documento e clique nele para iniciar o download
    document.body.appendChild(link);
    link.click();

    // Remova o link do documento
    document.body.removeChild(link);
  } catch (error) {
    console.error('Erro ao baixar os arquivos', error);
  }
};

const downloadAndDisplayImage = async () => {
      try {
        const body = {
          text: text.value
        }

        // Faça uma solicitação GET para a rota que fornece a imagem
        const response = await axios.post('/image', body, {
          responseType: 'arraybuffer',
        });

        // Crie um objeto Blob com os dados da resposta
        const blob = new Blob([response.data], { type: 'image/png' });

        // Crie uma URL de dados para a imagem Blob
        const blobUrl = URL.createObjectURL(blob);

        // Atualize as referências no estado
        imageBlob.value = blob;
        imageBlobUrl.value = blobUrl;
      } catch (error) {
        console.error('Erro ao baixar a imagem', error);
      }
    };
</script>

<template>
  <div class="bg-primary flex flex-row w-screen">
    <div :class="{ [`w-2/5`]: isShowResult }" class="flex flex-col gap-3 justify-center items-center h-screen w-full">
      <button type="button" v-if="isShowResult" class="absolute top-0 left-0 p-4" @click="goBack">
        <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24" fill="white">
          <path d="M400-80 0-480l400-400 71 71-329 329 329 329-71 71Z" />
        </svg>
        <span class="sr-only">Voltar</span>
      </button>

      <p class="text-white font-bold mb-6">Crie seu próprio e-commerce ✌🏻</p>

      <textarea spellcheck="false" id="message" rows="6" v-model="text" style="resize: none;"
        class="block p-2.5 w-[33vw] text-sm bg-secondary text-white text-bold marker:rounded-lg border border-accent2 rounded-xl placeholder:italic placeholder:text-lg"
        placeholder="Descreva aqui sua loja...&#10;”Quero um website para vender produtos variados, como itens para casa e eletrônicos”"></textarea>

      <button class="bg-accent w-[33vw] p-4 rounded-xl text-white" @click="showResult" v-if="!loading">
        {{ isShowResult ? "Baixar" : "Continuar" }}
      </button>
      <div role="status" v-else>
          <svg aria-hidden="true" class="w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-accent" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
              <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
          </svg>
          <span class="sr-only">Loading...</span>
      </div>
    </div>

    <div class="flex flex-col justify-center items-center h-screen w-3/5 bg-accent" v-if="isShowResult">
      <div v-if="imageBlob" class="px-6">
        <img :src="imageBlobUrl" alt="Imagem Baixada">
      </div>
    </div>
  </div>
</template>
