<template>
  <quill-editor v-model:value="value"
  ></quill-editor>
</template>

<script lang="ts">
export default {
  name: "RichText"
}
</script>
<script setup lang="ts">
import {defineProps, ref, defineEmits, computed} from "vue";

const props = defineProps({
  modelValue: String
})
const toolbar = ref(null)
const emits = defineEmits(['update:modelValue'])
const value = computed<string>({
  get: () => props.modelValue as string,
  set: () => emits('update:modelValue', value)
})
</script>
<style scoped>

</style>