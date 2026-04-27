module.exports = function(grunt) {
  require("load-grunt-tasks")(grunt);

  grunt.initConfig({
    pkg: grunt.file.readJSON("package.json"),

    concat: {
      dist: {
        src: [
          "js/libs/prism.js",
          "js/content-as-ecommerce.js",
          "js/jacobworsoe.js",
          "js/drinksberegner.js",
          "js/chart-bitcoin.js"
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
          implementation: require("sass"),
          outputStyle: "compressed",
          sourceMap: false
        },
        files: {
          "assets/css/main.css": "scss/main-bundle.sass"
        }
      }
    }
  });

  grunt.registerTask("build", ["sass", "concat", "uglify"]);
  grunt.registerTask("default", ["build"]);
};
