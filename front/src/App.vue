<template>
  <div v-if="component">
    <components-creator v-model="component"></components-creator>
  </div>
  <div>
  </div>

</template>
<script setup lang="ts">
import {useCMSStore} from "@/store/cms";
import {defineAsyncComponent, ref} from 'vue'
import {useRoute} from 'vue-router'
import ComponentsCreator from "@/components/ComponentsCreator.vue";
import TestComponent from "@/components/TestComponent.vue";

const testList = ref([
  {
    sequence_number: 0, name: '0', children: [{sequence_number: 1, name: '1'},
      {sequence_number: 2, name: '2'},
      {sequence_number: 3, name: '3'},
      {sequence_number: 4, name: '4'},
      {sequence_number: 5, name: '5'},]
  },
  {sequence_number: 1, name: '1'},
  {sequence_number: 2, name: '2'},
  {sequence_number: 3, name: '3'},
  {sequence_number: 4, name: '4'},
  {sequence_number: 5, name: '5'},
])
const layoutStore = useCMSStore();
const router = useRoute();
let component = ref();
layoutStore.getPage(router.path).then(res => {
  component.value = res
})
</script>
<style>

</style>