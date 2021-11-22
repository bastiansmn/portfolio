<template>
	<div class="AboutSlot">
		<slot name="content">

		</slot>
		<slot name="switcher">
		
		</slot>
	</div>
</template>

<script>
import Switcher from "./Switcher.vue";

export default {
	name: "AboutSlot",
	components: {
		Switcher
	},
	methods: {
		
	},
	data() {
		return {
			showLanguages: false,
		}
	},
}
</script>

<style scoped>
.AboutSlot {
	position: relative;
	width: 90%;
	height: 70vh;
	z-index: 10;
}
</style>