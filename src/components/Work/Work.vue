<template>
	<div class="Work">
		<!-- Bubbles -->
		<div class="bubble white-gradient __medium" style="
			left: -150px;
			bottom: 0;
			--xmove: -10px !important;
			--ymove: -5px !important;
		"></div>
		<div class="bubble blue-gradient __small" style="
			left: 20px;
			bottom: 120px;
			--xmove: 7px !important;
			--ymove: 2px !important;
		"></div>
		<div class="bubble blue-gradient __medium" style="
			right: -160px;
			bottom: 110px;
			--xmove: -10px !important;
			--ymove: -5px !important;
		"></div>
		<div class="bubble blue-gradient __small" style="
			right: 0;
			bottom: 270px;
			--xmove: -10px !important;
			--ymove: -5px !important;
		"></div>
		<div class="bubble blue-gradient __small" style="
			left: 10px;
			top: 50px;
			--xmove: -10px !important;
			--ymove: -5px !important;
		"></div>

		<!-- TODO : Factor le carroussel dans un component -->
		<div class="carroussel">
			<h1>
				{{
					this.getLang
						? text.projects.title.en
						: text.projects.title.fr
				}}
			</h1>

			<div class="slider reveal-btt" @scroll.prevent ref="slider">
				<div 
					class="projects">
					<a 
						:href="proj.project_link"
						target="blank"
						:key="proj.class"
						v-for="proj in work"
						class="project"
						:class="proj.class"
					>
						<div class="blur__effect">
							<div class="text-content">
								<h1 style="margin-top: 0">{{ proj.name }}</h1>
								<p>
									{{
										this.getLang 
											? proj.description.en
											: proj.description.fr	
									}}
								</p>
								<h3>
									{{  
										this.getLang
											? text.projects.contenth3.en
											: text.projects.contenth3.fr
									}}
								</h3>
								<div class="techs-used">
									<div 
										class="tech"
										:key="tech"
										v-for="tech in proj.techs"
									>
										<img :src="`logos/${tech}.png`" alt="">
									</div>
								</div>
							</div>
						</div>
						<div class="image">
							<img :src='`work/${proj.class}.png`' alt="">
						</div>
					</a>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import { mapGetters } from 'vuex';
import text from "../../assets/text.js";
import work from "../../assets/work.js";

export default {
	name: "Work",
	components: {
		
	},
	computed: {
		...mapGetters(["getLang"]),
	},
	methods: {
		
	},
	mounted() {
		
	},
	data() {
		return {
			currentSlide: 0,
			slideEnabled: true,

			text,
			work
		}
	},
}
</script>

<style scoped lang="scss">
.Work {
	position: relative;

	width: 90%;
	min-height: 80vh;

	display: flex;
	align-items: center;
	justify-content: center;
}

.carroussel {
	position: relative;

	width: 90%;
	height: 70vh;

	& > h1 {
		color: var(--primary);
		width: 90%;
	}

	& > .slider {
		position: relative;

		box-shadow: 20px 20px 50px rgba(0, 0, 0, .5);

		width: 100%;
		height: calc(100% - 73px);

		display: flex;
		align-items: center;
		justify-content: center;

		& > .projects {
			height: 100%;

			display: flex;
			flex-direction: row;
			align-items: center;
			justify-content: flex-start;

			overflow-x: scroll;

			& > .project {
				height: 100%;
				max-height: 100%;
				aspect-ratio: 16/9;
				color: var(--white);
				position: relative;

				& > .blur__effect {
					position: absolute;
					height: 100%;
					width: 100%;
					opacity: 0;
					background: hsl(0, 0%, 0%, .5);
					visibility: hidden;
					z-index: 100;

					& > .text-content {
						position: absolute;
						right: 20px;
						bottom: 20px;

						width: 500px;
						padding: 40px;

						background: rgba(12, 12, 19, 0.9);

						backdrop-filter: blur(10px);

						border-radius: 10px;
						

						& > h3 {
							display: flex;
							flex-direction: row;
							align-items: center;
							justify-content: flex-end;
							text-decoration: underline;
						}

						& > .techs-used {
							width: 100%;
							display: flex;
							flex-direction: row-reverse;
							align-items: center;
							justify-content: flex-start;
							height: 50px;
							
							& > .tech {
								height: 100%;
								aspect-ratio: 1;

								& > img {
									height: 100%;
									aspect-ratio: 1;
									margin-inline: 10px;
								}
							}
						}
					}
				}

				&:hover {					
					& > .image {
						& > img {
							transform: scale(1.03);
						}
					}

					& > .blur__effect {
						opacity: 1;
						visibility: visible;
					}
				}

				& > .image { 

					overflow: hidden;
					height: 100%;
					width: 100%;
				
					& > img {
						width: 100%;
						height: 100%;
						aspect-ratio: 16/9;
					}
				}
			}
		}
	}
}

/* Use scoll-snap-align only in firefox */
@-moz-document url-prefix() {
	.projects {
		scroll-snap-type: x mandatory;

		& > .project {
			scroll-snap-align: start;
		}
	}
}

@keyframes anim-button {
	0% {
		transform: translateX(0);
	}
	50% {
		transform: translateX(var(--toX));
	}
	100% {
		transform: translateX(0);
	}
}
</style>