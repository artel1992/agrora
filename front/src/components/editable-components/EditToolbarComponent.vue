<template>
  <div class="editor">
    <div v-if="!move">
      <i class='bx bxs-edit-alt action-icon' @click="emits('edit')"></i>
      <i class='bx bxs-save action-icon' @click="emits('save')"></i>
<!--      <i class='bx bx-plus action-icon' @click="emits('add')"></i>-->
      <i class='bx bxs-trash-alt action-icon' @click="emits('delete')"></i>
      <i class='bx bx-move  action-icon' @click="onMove"></i>
    </div>
    <div v-else>
      <i class='bx bxs-save action-icon'></i>
      <i class='bx bx-x action-icon' @click="move=false"></i>
    </div>
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


const move = ref(false)
const emits = defineEmits<{
  (eventName: 'edit'): void

  (eventName: 'save'): void

  (eventName: 'add'): void

  (eventName: 'delete'): void

  (eventName: 'move'): void
}>()
const store = useCMSStore();
const onMove = () => {
  emits('move')
  move.value = true
}
</script>

<style scoped>
.editor {
  @apply absolute top-0 right-0 bg-blue-600 bg-white/40 px-2 py-1 text-xl text-zinc-700 rounded-bl-lg divide-x divide-zinc-400/10 shadow-md z-50;
}

.editor .action-icon {
  @apply p-2 cursor-pointer hover:text-zinc-900;
}
</style>