<template>
	<div class="SoftSkills">
		<div class="text">
			<div class="soft_skills">
				<h1>
					{{
						this.getLang
							? text.soft_skills.title.en
							: text.soft_skills.title.fr
					}}
				</h1>
				<p>
					{{
						this.getLang
							? text.soft_skills.text.en
							: text.soft_skills.text.fr
					}}
				</p>
			</div>

			<Switcher @switch="$emit('switch')" />
		</div>
		<div class="soft_skills__list tilting reveal-rtl">
			<span class="card-title">
				{{
					this.getLang
						? text.soft_skills.card.title.en
						: text.soft_skills.card.title.fr
				}}
			</span>
			<ul>
				<li :key="sk" v-for="sk in soft_skills">
					<img :src="`icons/${sk.name}.png`" alt="">
					<span>
						{{ this.getLang 
						? sk.en
						: sk.fr }}
					</span>
				</li>
			</ul>
			<div class="resume">
						<a href="">
							{{ 
								this.getLang
									? text.resume.en
									: text.resume.fr
							}}
						</a>
					</div>
		</div>
	</div>
</template>

<script>
import text from "../../assets/text.js";
import soft_skills from "../../assets/soft_skills.js";
import { mapGetters } from "vuex";
import Switcher from "./Switcher.vue";

export default {
	name: "SoftSkills",
	components: {
		Switcher,
	},
	data() {
		return {
			soft_skills,
			text
		}
	},
	computed: {
		...mapGetters(['getLang'])
	}
}
</script>

<style scoped>
.SoftSkills {
	width: 90%;
	height: 500px;
	padding: 20px;

	display: flex;
	flex-direction: row;
	justify-content: space-between;
	align-items: center;
}

.SoftSkills > div {
	max-width: calc(42% - 40px);
	height: 100%;
}

.soft_skills__list {
	min-width: calc(40% - 44px);
	max-width: calc(40% - 44px);
	height: 90%;
   margin-block: 10px;
   background: rgba(255, 255, 255, 0.2);
   box-shadow: 20px 20px 50px rgba(0, 0, 0, .5);
   backdrop-filter: blur(13px);
   border-radius: 21px;

   z-index: 1000;

	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: space-between;

   padding: 35px;
	transform: rotateY(-4deg);
}

.soft_skills__list > * {
	width: 100%;
}

.soft_skills__list > ul {
	display: flex;
   flex-direction: column;
   align-items: flex-start;
   justify-content: space-between;
	list-style: none;
	widows: 100%;
	height: 70%;
	margin-bottom: 0;
	margin-top: 0;
	padding-left: 0;
}

.soft_skills__list > ul > li {
	width: 90%;
	height: 40px;
	display: flex;
	flex-direction: row;
	align-items: center;
	justify-content: flex-start;
	padding: 10px 10px 10px 17px;
	border-radius: 5px;
	font-size: 18px;
}

.soft_skills__list > ul > li:hover {
	background-color: var(--primary);
}

.soft_skills__list > ul > li > img {
	height: 70%;
	aspect-ratio: 1;
	margin-right: 20px;
}

.card-title {
	height: 30px;
	font-size: 24px;
	font-weight: bold;
}

.resume {
   width: 100%;
   height: 40px;
   display: flex;
   align-items: center;
   justify-content: center;
}

.resume > a {
   height: 30px;
   display: flex;
   align-items: center;
   justify-content: center;
   background-color: var(--primary);
   border-radius: 6px;
   padding-inline: 10px;
   color: var(--white);
   text-decoration: none;
   font-size: 14px;
}

.resume > a:hover {
   transform: scale(1.03);
}

.text {
	position: relative;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: space-between;
}
</style>