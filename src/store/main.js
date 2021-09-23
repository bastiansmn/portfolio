import {createStore} from "vuex";

export default createStore({
    state: {
        eng: false,
        enableObserver: true
    },
    mutations: {
        SWITCH_LANG(state) {
            state.eng = !state.eng;
        },
        SET_LANG(state, english) {
            state.eng = english;
        },
        SET_OBSERVER(state, enableObserver) {
            state.enableObserver = enableObserver;
        }
    },
    actions: {
        switchLang(context) {
            context.commit('SWITCH_LANG');
        },
        setLang(context, english=false) {
            context.commit('SET_LANG', english);
        },
        setObserver(context, enable) {
            context.commit('SET_OBSERVER', enable);
        }
    },
    getters: {
        getLang: state => {
            return state.eng;
        },
        observerEnabled: state => {
            return state.enableObserver;
        }
    }
})