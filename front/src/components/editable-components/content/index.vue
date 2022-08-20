<template>
  <div v-if="modelValue" v-html="modelValue.structure.props.content"></div>
</template>

<script lang="ts">
export default {
  name: "ContentComponent"
}
</script>
<script setup lang="ts">
import {defineProps} from "vue";

const props = defineProps({modelValue: Object})

</script>
<style>
@import "quill/dist/quill.core.css";
</style>