<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

const baseURL = 'http://127.0.0.1:8000' // sse API

const API = axios.create({
  baseURL,
  timeout: 300000,
})
const props = defineProps<{
  msg: string
}>()

const msg = ref(props.msg)

async function callApi() {
  const response = await API.get("/", {
    responseType: 'stream',  // This is critical for Axios streaming
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'text/event-stream'
    },
    adapter: 'fetch',
  });
  const stream = response.data;
  const reader = stream.pipeThrough(new TextDecoderStream()).getReader();
  let buffer = '';
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    buffer += value;
    const lines = buffer.split('\n');
    buffer = lines.pop() || '';

    lines.forEach(line => {
      if (line.startsWith('data:')) {
        const dataContent = line.substring(5).trim();
        msg.value += dataContent + '\n';


      }
    });
  }
}
</script>

<template>
  <div class="greetings">
    <h3 class="green">{{ msg }}</h3>

    <button class="big-button" @click="callApi">Call API</button>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 600px) {

  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}

.big-button {
  font-size: 1.5rem;
  padding: 10px 20px;
}
</style>
