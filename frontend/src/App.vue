<template>
  <NavBar />
  <ElementTable />
</template>

<script>
import NavBar from './components/NavBar.vue'
import ElementTable from './components/Table.vue';

export default {
  name: 'App',
  components: {
    NavBar,
    ElementTable
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
</style>
