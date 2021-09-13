<template>
   <navbar />
   <div class="portfolio__content">
      <div class="section" id="home" style="height: 110px;"></div>
      <Home data-color="blue" />
      <div id="about" class="section">
         <About />
      </div>
      <div id="work" class="section"></div>
      <div id="contact" class="section"></div>
   </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import Home from "./components/Home/Home.vue";
import {mapActions, mapGetters} from "vuex";
import setActive from "./utils/function";
import "kursor";
import About from "./components/About/About.vue";

export default {
   components: {
      About,
      Navbar,
      Home
   },
   beforeMount() {
      navigator.language !== "fr-FR" && this.setLang(true);
   },
   mounted() {
      const anchors = document.querySelectorAll('.section');
      const observer = new IntersectionObserver((entries) => {
         entries.forEach(entry => {
            console.log(entry);
            if (entry.isIntersecting && this.observerEnabled) {
               location.hash = `#${entry.target.id}`
               setActive(entry.target.id);
            }
            if (entry.target.id === 'home')
               document.querySelector(".navbar")
                     .classList.remove("navbar__background");
            if (entry.target.id !== 'home')
               document.querySelector(".navbar")
                     .classList.add("navbar__background");
         });
      }, {
         threshold: .55
      });
      anchors.forEach(anchor => {
         observer.observe(anchor)
      });

      window.addEventListener("mousewheel", _ => {
         this.setObserver(true);
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
</style>
