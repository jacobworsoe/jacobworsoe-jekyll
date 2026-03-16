module.exports = function(grunt) {
  require("load-grunt-tasks")(grunt);

  grunt.initConfig({
    pkg: grunt.file.readJSON("package.json"),

    concat: {
      dist: {
        src: [
          "js/libs/prism.js",
          "js/content-as-ecommerce.js",
          "js/tracking.js",
          "js/jacobworsoe.js",
          "js/drinksberegner.js"
        ],
        dest: "assets/js/bundle.js"
      }
    },

    uglify: {
      build: {
        files: [{
          src: "assets/js/bundle.js",
          dest: "assets/js/bundle.min.js"
        }]
      }
    },

    sass: {
      dist: {
        options: {
          style: "compressed",
          sourcemap: "none"
        },
        files: {
          "assets/css/homepage.css": "scss/homepage-bundle.sass",
          "assets/css/single.css": "scss/single-bundle.sass"
        }
      }
    }
  });

  grunt.registerTask("build", ["sass", "concat", "uglify"]);
  grunt.registerTask("default", ["build"]);
};
