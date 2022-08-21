<template>
  <div v-if="component">
    <components-creator v-model="component"></components-creator>
  </div>
  <div>
  </div>

</template>
<script setup lang="ts">
import {useCMSStore} from "@/store/cms";
import {ref} from 'vue'
import {useRoute} from 'vue-router'
import ComponentsCreator from "@/components/ComponentsCreator.vue";

const cmsStore = useCMSStore();
const router = useRoute();
let component = ref();
cmsStore.getPage(router.path).then(res => {
  component.value = res
})
</script>
<style>

</style>