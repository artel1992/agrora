<template>
  <div class="max-h-[80vh]">
    <quill-editor v-model:content="valueTest"
                toolbar="full"
                content-type="html"
                placeholder="..."
  ></quill-editor>
  </div>
</template>

<script lang="ts">
export default {
  name: "RichText"
}
</script>
<script setup lang="ts">
import {defineProps, ref, defineEmits, computed} from "vue";

const props = defineProps({
  value: String
})
const toolbar = ref(null)
const emits = defineEmits(['update:value'])
const valueTest = computed<string>({
  get: () => props.value as string,
  set: (v) => emits('update:value', v)
})
</script>
<style scoped>

</style>