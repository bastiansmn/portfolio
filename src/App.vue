<template>
   <navbar />
   <div class="portfolio__content">
      <div class="section" id="home" style="height: 110px;"></div>
      <Home class="home" />
      <div id="about" class="section">
         <About />
      </div>
      <div id="work" class="section">
			<Work />
		</div>
      <div id="contact" class="section">
			<Contact />
		</div>
   </div>
</template>

<script>
import vanillaTilt from "vanilla-tilt";
import Navbar from "./components/Navbar.vue";
import Home from "./components/Home/Home.vue";
import {mapActions, mapGetters} from "vuex";
import setActive from "./utils/function";
import About from "./components/About/About.vue";
import Work from "./components/Work/Work.vue";
import Contact from "./components/Contact/Contact.vue";

export default {
   components: {
      About,
      Navbar,
      Home,
		Work,
		Contact
   },
   beforeMount() {
      !"fr-FR".includes(navigator.language) && this.setLang(true);
   },
   mounted() {
      const anchors = document.querySelectorAll('.section');
      const observer = new IntersectionObserver((entries) => {
         entries.forEach(entry => {
            if (entry.isIntersecting) {
               if (this.observerEnabled) {
                  location.hash = `#${entry.target.id}`
                  setActive(entry.target.id);
               }
					if (entry.target.id === "home") {
						document.querySelector(".home").classList.add("section_active");
                  document.querySelector(".navbar").classList.remove("navbar__background");
					} else {
						entry.target.classList.add("section_active");
                  document.querySelector(".navbar").classList.add("navbar__background");
					}
            } else {
					if (entry.target.id === "home") {
						document.querySelector(".home").classList.remove("section_active");
					} else {
						entry.target.classList.remove("section_active");
					}
				}
         });
      }, {
         threshold: .55
      });
      anchors.forEach(anchor => {
         observer.observe(anchor)
      });

// TODO : Vérifier si tout fonctionne bien avec une souris
      window.addEventListener("mousewheel", _ => {
         this.setObserver(true);
      });
		window.addEventListener("DOMMouseScroll", _ => {
			this.setObserver(true);
		})

		vanillaTilt.init(document.querySelectorAll(".tilting"), {
         max: 7,
         speed: 1000,
         perspective: 700,
         reverse: true,
         reset: false,
         startX: 7,
         startY: -5,
      });
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
   computed: {
      ...mapGetters(['observerEnabled'])
   },
   methods: {
      ...mapActions(['setLang', 'setObserver'])
   },
}
</script>

<style>

#about, #work, #contact {
   min-height: 700px;
}

.portfolio__content {
   width: 100vw;
   height: 100vh;
   
   overflow-y: auto;
   overflow-x: hidden;
}

/* Use scoll-snap-align only in firefox */
@-moz-document url-prefix() {
	.portfolio__content {
		scroll-snap-type: y mandatory;

		width: 100vw;
		height: 100vh;
		
		overflow-y: auto;
		overflow-x: hidden;
	}

	
	.section {
		scroll-snap-align: start;
	}
}

.section {
	display: flex;
	align-items: center;
	justify-content: center;

	position: relative;
}


#contact {
	margin-top: 110px;
	height: calc(100vh - 110px);
}
</style>
