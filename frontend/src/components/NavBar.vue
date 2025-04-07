<template>
  <div class="nav-bar">
    <div class="nav-bar-logo">
      <img :src="`Raven-02.png`" alt="Logo">
    </div>
    <div class="nav-bar-search">
      <input id="search-bar" type="text" placeholder="Search">
    </div>
    <p>Purchase</p>
    <div class="nav-bar-switch">
      <label class="nav-bar-switch">
        <input id="toggle" v-on:click="stateChange" type="checkbox">
        <span class="slider round"></span>
      </label>
    </div>
    <p>Note</p>
  </div>
</template>

<script>
  export default {
    name: 'NavBar',
    data() {
      return {
        state: 'purchase',
        login: false
      }
    },
    // mounted() {
    //   fetch('http://localhost:8000/api/elements/')
    //     .then(response => response.json())
    //     .then(data => {
    //       this.elements = data;
    //     });
    // }
    methods: {
      stateChange() {
        if (this.state === 'purchase') {
          this.state = 'note'
          console.log(this.state)
        } else {
          this.state = 'purchase'
          console.log(this.state)
        }
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
* {
  padding: 0;
  margin: auto;
  box-sizing: border-box;
}
.nav-bar {
  margin: auto;
  position: fixed;
  display: flex;
  flex-flow: nowrap;
  justify-content: space-between;
  padding: 10px;
  color: #1E2237;
  background-color: white;
  border-radius: 0 0 7px 7px;
  width: 70vw;
  height: 60px;
  transform: translateX(50%);
  right: 50%;
}
.nav-bar-logo {
  padding-right: 10%;
}
.nav-bar-logo img {
  width: 40px;
}
.nav-bar-search {
  width: 50% !important;
}
.nav-bar-search input {
  width: 100%;
  padding: 10px;
  border: 1px solid #1E2237;
  border-radius: 5px;
}
.nav-bar-switch {
  position: relative;
  display: flex;
  width: 30px;
  height: 17px;
}
.nav-bar-switch input {
  opacity: 0;
  width: 0;
  height: 0;
}
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: .4s;
  transition: .4s;
}
.slider:before {
  position: absolute;
  content: "";
  height: 13px;
  width: 13px;
  left: 2px;
  bottom: 2px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked + .slider {
  background-color: #2196F3;
}
input:focus + .slider {
  box-shadow: 0 0 1px #2196F3;
}
input:checked + .slider:before {
  -webkit-transform: translateX(13px);
  -ms-transform: translateX(13px);
  transform: translateX(13px);
}
.slider.round {
  border-radius: 34px;
}
.slider.round:before {
  border-radius: 50%;
}
</style>
