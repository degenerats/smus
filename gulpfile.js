var postcss = require('gulp-postcss');
var gulp = require('gulp');
var autoprefixer = require('autoprefixer');
var cssnano = require('cssnano');
var watch = require('gulp-watch');
var rename = require("gulp-rename");

var postcss_proc = [
    autoprefixer({browsers: ['last 1 version']}),
    cssnano(),
    require('precss')({ /* options */ })
];

gulp.task('css', function () {
    return gulp.src('**/css/components/**/source/*.css')
        .pipe(postcss(postcss_proc))
        .pipe(rename(function (path) {
          path.dirname = path.dirname.replace('/source', '')
        }))
        .pipe(gulp.dest('./'))
});

gulp.task('default', function () {
    return gulp.src('**/css/components/**/source/*.css')
        .pipe(watch('**/css/components/**/source/*.css'))
        .pipe(postcss(postcss_proc))
        .pipe(rename(function (path) {
          path.dirname = path.dirname.replace('/source', '')
        }))
        .pipe(gulp.dest('./'))
});
