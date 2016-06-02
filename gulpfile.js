var postcss = require('gulp-postcss');
var gulp = require('gulp');
var autoprefixer = require('autoprefixer');
var cssnano = require('cssnano');
var watch = require('gulp-watch');
var rename = require("gulp-rename");
var coffee = require('gulp-coffee');
var uglify = require('gulp-uglify');
var sourcemaps = require('gulp-sourcemaps');
var concat = require('gulp-concat');
var del = require('del');

var postcss_proc = [
    autoprefixer({browsers: ['last 1 version']}),
    cssnano(),
    require('precss')({ /* options */ })
];

var paths = {
  styles: "**/css/components/**/source/*.css",
  scripts: "static/js/source/*.coffee"
};

gulp.task('styles', function () {
    return gulp.src(paths.styles)
        .pipe(postcss(postcss_proc))
        .pipe(rename(function (path) {
          path.dirname = path.dirname.replace('/source', '')
        }))
        .pipe(gulp.dest('./'))
});

gulp.task('scripts', function() {
  return gulp.src(paths.scripts)
    .pipe(sourcemaps.init())
      .pipe(coffee())
      .pipe(rename(function (path) {
        path.dirname = path.dirname.replace('/source', '')
      }))
      .pipe(concat('scripts.min.js'))
    .pipe(sourcemaps.write())
    .pipe(gulp.dest('static/js'));
});

// Rerun the task when a file changes
gulp.task('watch', function() {
  gulp.watch(paths.scripts, ['scripts']);
  gulp.watch(paths.styles, ['styles']);
});

gulp.task('default', ['watch', 'scripts', 'styles']);
