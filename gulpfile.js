var postcss = require('gulp-postcss');
var gulp = require('gulp');
var autoprefixer = require('autoprefixer');
var cssnano = require('cssnano');
var watch = require('gulp-watch');

var postcss_proc = [
    autoprefixer({browsers: ['last 1 version']}),
    cssnano(),
    require('precss')({ /* options */ })
];

gulp.task('css', function () {
    return gulp.src('./app/static/css/components/source/*.css')
        .pipe(postcss(postcss_proc))
        .pipe(gulp.dest('./app/static/css/components/'));
});

gulp.task('default', function () {
    return gulp.src('./app/static/css/components/source/*.css')
        .pipe(watch('./app/static/css/components/source/*.css'))
        .pipe(postcss(postcss_proc))
        .pipe(gulp.dest('./app/static/css/components/'));
});
