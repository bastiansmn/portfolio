<template>
	<div class="AboutSlot">
		<slot name="content"> </slot>
		<slot name="switcher"> </slot>
	</div>
</template>

<script>
import Switcher from "./Switcher.vue";

export default {
	name: "AboutSlot",
	components: {
		Switcher,
	},
	methods: {},
	data() {
		return {
			showLanguages: false,
		};
	},
};
</script>

<style scoped>
@media screen and (max-width: 931px) {
	.AboutSlot {
		height: 100%;
	}
}

@media screen and (min-width: 930px) {
	.AboutSlot {
		height: 70vh;
	}
}

.AboutSlot {
	position: relative;
	width: 90%;
	z-index: 10;
}
</style>