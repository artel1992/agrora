<template>
  <div v-if="pages" class="flex px-10 py-5">
    <div v-for="(page,ind) in pages" :key="page.name"
         class="bg-blue-50 text-blue-600 w-40 px-4 py-2 rounded-lg shadow-md text-center space-y-4">
      <span>{{ page.title }}</span>
      <input type="text" placeholder="Путь" class="w-full" v-model="pages[ind].path">
      <button class="bg-blue-600 text-blue-50 rounded-md px-2 py-1" @click="createPage(pages[ind])">Создать</button>
    </div>
  </div>
</template>

<script lang="ts">
export default {
  name: "PageCreator"
}
</script>
<script setup lang="ts">
import {onMounted, ref, defineEmits} from "vue";
import {EditableComponent} from "@/core/interfaces";
import {useCMSStore} from "@/store/cms";

const emits = defineEmits<{ (eventName: 'create'): void }>()
const {getPages, createComponent} = useCMSStore();
const pages = ref<EditableComponent<any>[]>()
onMounted(() => {
  getPages().then((res: EditableComponent<any>[]) => {
    pages.value = res
  })
})
const createPage = (page: EditableComponent<any>) => {
  createComponent(page)
  emits('create')
}
</script>

<style scoped>

</style>