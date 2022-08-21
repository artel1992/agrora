<template>
  <div class="toolbar">
    <input type="text" :value="title" @input="$emit('update:title', $event.target.value)">
    <select @input="addClass">
      <option v-for="item in configs.paddings.all" :value="item" :key="item">{{ item }}</option>
    </select>
  </div>
</template>

<script lang="ts">
export default {
  name: "ConfigForm"
}
</script>
<script setup lang="ts">
import {defineProps, defineEmits} from "vue";

const props = defineProps(['title', 'classes'])
const emits = defineEmits(['update:title', 'update:classes'])
const configs = {
  paddings: {
    all: ['p-small', 'p-middle', 'p-big'],
    bottom: ['pb-small', 'pb-middle', 'pb-big'],
    left: ['pl-small', 'pl-middle', 'pl-big'],
    right: ['pr-small', 'pr-middle', 'pr-big'],
    top: ['pr-small', 'pr-middle', 'pr-big'],
    horizontal: ['px-small', 'px-middle', 'px-big'],
    vertical: ['py-small', 'py-middle', 'py-big'],
  },

}
const addClass = (ev: any) => {
  const classes = {...props.classes}
  if (classes[ev.target.value])
    delete classes[ev.target.value]
  else
    classes[ev.target.value] = true
  emits('update:classes', classes)

}
</script>
<style scoped>

</style>