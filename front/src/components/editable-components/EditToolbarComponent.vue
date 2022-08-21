<template>
  <div class="editor">
    <i class='bx bxs-edit-alt action-icon' @click="emits('edit')"></i>
    <i class='bx bxs-save action-icon' @click="emits('save')"></i>
    <i class='bx bxs-cog action-icon' @click="emits('config')"></i>
    <i class='bx bxs-trash-alt action-icon' @click="emits('delete')"></i>
    <i class='bx bx-move action-icon'></i>
  </div>
</template>

<script lang="ts">
export default {
  name: "EditToolbarComponent"
}
</script>
<script setup lang="ts">
import {useCMSStore} from "@/store/cms";
import {ref, defineEmits} from "vue";


const emits = defineEmits<{
  (eventName: 'edit'): void
  (eventName: 'save'): void
  (eventName: 'add'): void
  (eventName: 'delete'): void
  (eventName: 'config'): void
  (eventName: 'move'): void
}>()
const store = useCMSStore();
</script>

<style scoped>
.editor {
  @apply absolute top-0 right-0 bg-blue-600 bg-white/40 px-2 py-1 text-xl text-zinc-700 rounded-bl-lg divide-x divide-zinc-400/10 shadow-md z-50;
}

.editor .action-icon {
  @apply p-2 cursor-pointer hover:text-zinc-900;
}
</style>