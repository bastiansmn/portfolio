<template>
	<div class="Languages">
		<!-- TODO -->
		<div class="techs reveal-ltr">
			<div class="card tilting-low">
				<div>
					<div
						:key="key"
						v-for="(value, key) of techs"
						:class="key"
					>
						<div
							:key="t.classname"
							v-for="t in value.slice(0, 4)"
							:class="t.classname"
						>
							<img :src="`logos/${t.classname}.png`" :alt="t.name">
							<span>
								{{ t.name }}
							</span>
						</div>
					</div>

				</div>
			</div>
		</div>
		<div class="text reveal-rtl">
			<div>
				<h2 style="color: var(--white); margin-top: 0" v-html="
					getLang
							? text.techs.h2.en
							: text.techs.h2.fr
				">
				</h2>
				<p v-html="
					getLang
							? text.techs.p1.en
							: text.techs.p1.fr
				">
				</p>
				<p v-html="
					getLang 
							? text.techs.p2.en
							: text.techs.p2.fr
				"></p>
			</div>
		</div>
	</div>
</template>

<script>
import { mapGetters } from 'vuex';
import text from "../../assets/text.js";
import vanillaTilt from "vanilla-tilt";
import techs from "../../assets/techs.js";

export default {
	name: "Languages",
	components: {
		
	},
	methods: {
		capitalizeFirstLetter(string) {
			return string.charAt(0).toUpperCase() + string.slice(1);
		}
	},
	computed: {
		...mapGetters(["getLang"])
	},
	mounted() {
		vanillaTilt.init(document.querySelectorAll(".tilting-low"), {
         max: 3,
         speed: 1000,
         perspective: 700,
         reverse: true,
         reset: false,
         startX: 4,
         startY: 0,
      });
	},
	data() {
		return {
			text,
			techs
		}
	},
}
</script>

<style scoped lang="scss">
.Languages {
	width: 100%;
	height: 100%;

	display: flex;
	flex-direction: row;
	align-items: center;
	justify-content: space-between;	

	& > div {
		height: 100%;
		width: 45%;
	}
}

.text > div {
	margin: 70px 50px;

	& > p:deep(span) {
		color: var(--primary)
	}
}

.techs {
	display: flex;
	justify-content: center;

	& > .card {
		margin-top: 5vh;
		height: calc(90% - 90px - 6vh);
		width: 90%;
		background: var(--glass);
		border-radius: 10px;
		
		box-shadow: 20px 20px 50px rgba(0, 0, 0, .5);

		& > div {
			margin: 30px;
			height: calc(100% - 60px);

			& > div { // Div containing categories
				height: 25%;
				width: 100%;
				display: flex;
				flex-direction: row;
				align-items: center;

				& > div { // Div containing a tech
					--padding: 10px;
					padding: var(--padding);				
					list-style: none;
					width: calc(25% - 2*var(--padding));
					height: calc(100% - 2*var(--padding));

					display: flex;
					flex-direction: column;
					align-items: center;
					justify-content: space-between;

					& > img {
						max-height: 50%;
						aspect-ratio: 1;
					}
				}
			}
		}
	}
}
</style>