<template>
	<div class="switcher">
		<span 
			:style="!type && { color: '#6C6C6C' }"
			@click="switcher = !switcher; $emit('switch')"
		>{{
				this.getLang
					? text.switcher.soft_skills.en
					: text.switcher.soft_skills.fr
			}}</span>
		<span>-</span>
		<span
			:style="type && { color: '#6C6C6C' }"
			@click="switcher = !switcher; $emit('switch')"
		>{{
				this.getLang 
					? text.switcher.languages.en
					: text.switcher.languages.fr
			}}</span>
	</div>
</template>

<script>
import { mapGetters } from 'vuex';
import text from "../../assets/text.js";

export default {
	name: "Switcher",
	data() {
		return {
			switcher: true,
			text
		}
	},
	computed: {
		...mapGetters(['getLang'])
	}
}
</script>

<style>
.switcher {
	height: 40px;
	width: 100%;
	display: flex;
	align-items: center;
	justify-content: center;
}

.switcher > span {
	width: 100%;
	font-size: 20px;
	margin-inline: 10px;
	min-width: 10%;
	width: 10%;
	display: flex;
	justify-content: center;
}

.switcher > span:nth-child(2n + 1) {
	cursor: pointer;
	font-size: 19px;
	min-width: 29%;
}
</style>