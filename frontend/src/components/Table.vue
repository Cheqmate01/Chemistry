<template>
  <div>
    <h1>Periodic Table</h1>
    <div class="table">
      <div v-for="element in elements" :key="element.id" :class="`element group${element.group}`">
        <div class="atomic_number">{{ element.atomic_number }}</div>
        <div class="symbol">{{ element.symbol }}</div>
        <div class="name">{{ element.name }}</div>
        <div class="atomic_weight">{{ element.atomic_weight }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ElementTable',
  data() {
    return {
      elements: []
    };
  },
  mounted() {
    fetch('http://localhost:8000/api/elements/')
      .then(response => response.json())
      .then(data => {
        this.elements = data;
      });
  }
}
</script>

<style scoped>
h1 {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.table {
  display: grid;
  grid-template-columns: repeat(18, auto);
  width: 100%;
  font-size: 8px;
}
.element {
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 1px solid black;
  padding: 7px 2px;
  background-color: #38B8E4;
}
.element .atomic_number, .element .atomic_weight {
  font-size: 10px;
}
.element .symbol {
  font-size: 20px;
}

/* Position elements based on their group */
.element.group1 { grid-column: 1; }
.element.group2 { grid-column: 2; }
.element.group3 { grid-column: 3; }
.element.group4 { grid-column: 4; }
.element.group5 { grid-column: 5; }
.element.group6 { grid-column: 6; }
.element.group7 { grid-column: 7; }
.element.group8 { grid-column: 8; }
.element.group9 { grid-column: 9; }
.element.group10 { grid-column: 10; }
.element.group11 { grid-column: 11; }
.element.group12 { grid-column: 12; }
.element.group13 { grid-column: 13; }
.element.group14 { grid-column: 14; }
.element.group15 { grid-column: 15; }
.element.group16 { grid-column: 16; }
.element.group17 { grid-column: 17; }
.element.group18 { grid-column: 18; }
</style>
