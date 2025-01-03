<template>
	<div class="SoftSkills">
		<div class="text reveal-ltr">
			<div>
				<h1>{{
						this.getLang 
							? text.soft_skills.title.en
							: text.soft_skills.title.fr
					}}</h1>
				<p>
					{{
						this.getLang
							? text.soft_skills.text.en
							: text.soft_skills.text.fr
					}}
				</p>
			</div>
		</div>
		<div class="soft_skills">
			<div class="card reveal-rtl tilting-low">
				<div>
					<h2 style="color: var(--primary)">
						{{
							this.getLang
								? text.soft_skills.card.title.en
								: text.soft_skills.card.title.fr
						}}
					</h2>
					<ul class="list-soft_skills">
						<li :key="e" v-for="e in soft_skills">
							<img :src="`icons/${e.name}.png`" :alt="e.name">
							<span>
								{{
									this.getLang 
										? e.en
										: e.fr
								}}
							</span>
						</li>
						<li>
							<a target="_blank" href="https://drive.google.com/file/d/1NPITB52bzIIEpPpx71j9mw44I7cqQgjL/view">
								{{
									this.getLang
										? text.resume.en
										: text.resume.fr
								}}
							</a>
						</li>
					</ul>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import { mapGetters } from 'vuex';
import text from "../../assets/text.js";
import soft_skills from "../../assets/soft_skills.js";
import vanillaTilt from "vanilla-tilt";

export default {
	name: "SoftSkills",
	components: {
		
	},
	methods: {
		
	},
	computed: {
		...mapGetters(["getLang", "isMobile"]),
	},	
	data() {
		return {
			text,
			soft_skills,
		}
	},
	mounted() {
		vanillaTilt.init(document.querySelectorAll(".tilting-low"), {
         max: 3,
         speed: 1000,
         perspective: 700,
         reverse: true,
         reset: false,
         startX: -4,
         startY: 0,
      });
	},
}
</script>

<style scoped lang="scss">
@media screen and (max-width: 930px) {
	.SoftSkills {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: flex-start;
		min-height: calc(100% - 100px);
		max-height: calc(100% - 100px);
		
		& > div {
			width: 100%;
		}

		& > .text > div {
			& > p {
				font-size: min(2.5vh, 17px);
			}
			& > h1 {
				font-size: min(6vh, 40px);
			}
		}
		& > .soft_skills {
			margin-block: 3vh;
		
			& > .card {
				width: 100%;
				height: 100%;

				& > div {
					margin: 15px;

					& > h2 {
						display: none;
					}

					& > ul > li {
						height: 5vh;
					}
				}
			}
		}
	}
}

@media screen and (min-width: 931px) {
	.SoftSkills {
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: space-between;
		height: 100%;

		& > div {
			width: 45%;
			height: 100%;
		}

		& > .text > div {
			margin: 10vh 50px;
		}
	}

	.card > div {
		height: calc(100% - 80px);	
	}

	.list-soft_skills {
		height: calc(100% - 50px);
	}
}

.SoftSkills {
	width: 100%;
}

.soft_skills {
	display: flex;
	align-items: center;
	justify-content: center;
}

.card {
	height: 80%;
	width: 90%;
	background: var(--glass);
	border-radius: 10px;
	
	box-shadow: 20px 20px 50px rgba(0, 0, 0, .5);

	& > div {
		margin: 40px;
	}
}

.list-soft_skills {
	list-style: none;
	padding: 0;
	margin: 0;

	display: flex;
	align-items: flex-start;
	justify-content: space-between;
	flex-direction: column;

	& > li:not(:last-child) {
		width: calc(100% - 20px);
		height: 45px;
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: flex-start;
		padding-inline: 10px;
		background: none;
		border-radius: 7px;
		transition: background .2s ease-out;
	}

	& > li > img {
		height: 65%;
		aspect-ratio: 1;
		margin-right: 20px;
	}

	& > li > span {
		font-size: min(2.5vh, 16px);
	}

	& > li:last-child {
		width: 100%;
		height: 35px;
		display: flex;
		align-items: center;
		justify-content: center;

		& > a {
 			text-decoration: none;
			border-radius: 4px;
			background: var(--primary);
			color: var(--white);
			padding-block: .8vh;
			padding-inline: 1.8vh;

			&:hover {
				transform: scale(1.02);
				background: var(--white);
				color: var(--primary);
			}
		}
	}
}

</style>