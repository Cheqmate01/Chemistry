<template>
  <NavBar />
  <StartSpace />
  <RouterView />
  <EndSpace />
  <FootLinks />
</template>

<script>
import NavBar from './components/NavBar.vue'
import StartSpace from './components/StartSpace.vue';
import EndSpace from './components/EndSpace.vue';
import FootLinks from './components/Footer.vue';
import { RouterView } from 'vue-router';

export default {
  name: 'App',
  components: {
    NavBar,
    StartSpace,
    RouterView,
    EndSpace,
    FootLinks,
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
