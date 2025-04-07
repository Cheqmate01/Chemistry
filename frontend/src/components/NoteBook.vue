<template>
    <div class="note-book">
        <div class="note-book-header">
            <h1>Note Book</h1>
        </div>
        <div class="note-book-content">
            <p v-if="element">Element Name: {{ element.name }}</p>
            <textarea v-if="element" :id="`${element.name}-note`" class="note-area" placeholder="Write your notes here..."></textarea>
        </div>
    </div>
</template>

<script>
export default {
    name: 'NoteBook',
    data() {
        return {
            element: null
        };
    },
    mounted() {
        this.fetchElement();
    },
    watch: {
        '$route.params.noteId': 'fetchElement'
    },
    methods: {
        fetchElement() {
            const noteId = this.$route.params.noteId;
            if (noteId) {
                fetch(`http://localhost:8000/api/elements/?id=${noteId}`)
                    .then(response => response.json())
                    .then(data => {
                        this.element = data[0];
                    })
                    .catch(error => {
                        console.error('Error fetching element:', error);
                    });
            }
        }
    }
}
</script>

<style>
    .note-book {
        padding-top: 70px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .note-book-header {
        margin-bottom: 20px;
    }
    .note-book-content {
        width: 80%;
    }
    .note-area {
        width: 100%;
        height: 300px;
        border: none;
        border-bottom: 2px solid black;
        font-size: 15px;
        line-height: 1.5;
        line-break: anywhere;
        resize: none;
        outline: none;
        padding: 10px;
        box-sizing: border-box;
    }
</style>