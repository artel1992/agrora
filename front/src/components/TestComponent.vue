<template>
  <span>1</span>
  <draggable
      :list="list"
      item-key="sequence_number"
  >
    <template #item="{ element }" >
      <div>
        <p>{{ element.name }}</p>
        <test-component v-if="element.children" :list="element.children"/>
      </div>
    </template>
  </draggable>
</template>

<script lang="ts">


export default {
  name: "TestComponent",
  props: {list: {type: Array, default: () => []}},
}
</script>
<script setup lang="ts">
import draggable from "vuedraggable";
</script>
<style scoped>

</style>