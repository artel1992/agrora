<template>
  <div v-if="component">
    <components-creator v-model="component"></components-creator>
  </div>
  <div v-else>
    <page-creator @create="getComponents(router.path)"></page-creator>
  </div>
  <div>
  </div>

</template>
<script setup lang="ts">
import {useCMSStore} from "@/store/cms";
import {onMounted, ref} from 'vue'
import {useRoute} from 'vue-router'
import ComponentsCreator from "@/components/ComponentsCreator.vue";
import {EditableComponent} from "@/core/interfaces";
import PageCreator from "@/components/PageCreator.vue";

const {getComponents} = useCMSStore();
const router = useRoute();
let component = ref();
onMounted(() => {
  getComponents(router.path).then((res: EditableComponent<any>) => {
    component.value = res
  })
})
</script>
<style>

</style>