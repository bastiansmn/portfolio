<template>
	<div class="Work">
		<!-- TODO : Factor le carroussel dans un component -->
		<div class="carroussel">
			<h1>
				{{
					this.getLang
						? text.projects.title.en
						: text.projects.title.fr
				}}
			</h1>

			<!-- TODO : Faire que le scroll gère le carroussel (goToSlide(+1) si vers la droite etc) -->
			<div class="slider reveal-btt" ref="slider">
				<div class="projects">
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

				<button 
					:disabled="this.currentSlide === 0"
					@click="goToSlide(-1)"
					class="prev">
					<span></span>
					<span></span>
				</button>

				<button
					:disabled="this.currentSlide === this.work.length - 1"
					@click="goToSlide(+1)"
					class="next">
					<span></span>
					<span></span>
				</button>
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
		goToSlide(incr) {
			if (this.currentSlide + incr < this.work.length && this.currentSlide + incr >= 0)
				this.currentSlide += incr
		}
	},
	mounted() {
		
	},
	data() {
		return {
			currentSlide: 0,

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

		& > button {
			position: absolute;
			width: 40px;
			height: 50px;
			border: none;
			outline: none;
			border-radius: 5px;
			z-index: 101;

			& > span {
				display: block;
				width: 22px;
				height: 6px;
				border-radius: 3px;
			}
			
			&.next {
				--toX: 5px;
				right: 10px;
				& > span:nth-child(1) {
					transform-origin: bottom right;
					transform:
						translateY(4px)
						rotateZ(45deg);
				}
				& > span:nth-child(2) {
					transform-origin: top right;
					transform:
						translateY(-4px)
						rotateZ(-45deg);
				}
			}

			&.prev {
				--toX: -5px;
				left: 10px;
				& > span:nth-child(1) {
					transform-origin: bottom left;
					transform:
						translateX(4px)
						rotateZ(45deg);
				}
				& > span:nth-child(2) {
					transform-origin: top left;
					transform:
						translateX(4px)
						rotateZ(-45deg);
				}
			}

			&[disabled] {
				background: rgba(0, 0, 0, .2);
				cursor: initial;

				& > span {
					
					background: var(--dark-grey);
					border-radius: 3px;
				}
			}

			&:not([disabled]) {
				background: hsl(0, 0, 100, .2);
				cursor: pointer;

				&:hover {
					background: var(--primary);
					animation: anim-button 1s infinite;
				}

				& > span {
					background: var(--white);
				}
			}
		}


		& > .projects {
			height: 100%;

			display: flex;
			flex-direction: row;
			align-items: center;
			justify-content: flex-start;

			overflow-x: scroll;

			& > .project {
				height: 100%;
				aspect-ratio: 16/9;
				color: var(--white);
				position: relative;

				& > .blur__effect {
					position: absolute;
					height: 100%;
					width: 100%;
					opacity: 0;
					background: hsl(0, 0, 0, .5);
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