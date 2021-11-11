<template>
	<div class="Languages">
		<div class="text">

			<Switcher @switch="$emit('switch')" />
		</div>
		<div class="programming_langua"></div>
	</div>
</template>

<script>
import text from "../../assets/text.js";
import Switcher from "./Switcher.vue";

export default {
	name: "Languages",
	components: {
		Switcher,
	},
	data() {
		return {
			text
		}
	}
}
</script>

<style>
.Languages {
	width: 90%;
	height: 500px;
	padding: 20px;

	display: flex;
	flex-direction: row;
	justify-content: space-between;
	align-items: center;
}


</style>