<template>
    <div class="footer">
        <div class="foot-links">
            <table>
                <tbody>
                    <tr>
                        <td><a href="">opsum eltum</a></td>
                        <td><a href="">opsum eltum</a></td>
                        <td><a href="">opsum eltum</a></td>
                    </tr>
                    <tr>
                        <td><a href="">opsum eltum</a></td>
                        <td><a href="">opsum eltum</a></td>
                        <td><a href="">opsum eltum</a></td>
                    </tr>
                    <tr>
                        <td><a href="">opsum eltum</a></td>
                        <td><a href="">opsum eltum</a></td>
                        <td><a href="">opsum eltum</a></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'FootLinks',
        data() {return {}}
    }
</script>

<style>
.footer {
    background-color: black;
    color: aqua;
}
.foot-links {
    position: relative;
    width: 80%;
    padding-bottom: 100px;
    bottom: 0;
}
table tr {
    margin-right: 15%;
}
</style>