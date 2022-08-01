#include <chibi/eval.h>

void dostuff(sexp ctx) {
  // declare and preserve local variables *
  sexp_gc_var2(obj1, obj2);
  sexp_gc_preserve2(ctx, obj1, obj2);

  // load a file containing Scheme code *
  obj1 = sexp_c_string(ctx, "/path/to/source/file.scm", -1);
  sexp_load(ctx, obj1, NULL);

  // eval a C string as Scheme code *
  sexp_eval_string(ctx, "(some scheme expression)", -1, NULL);

  // construct a Scheme expression to eval *
  obj1 = sexp_intern(ctx, "my-procedure", -1);
  obj2 = sexp_cons(ctx, obj1, SEXP_NULL);
  sexp_eval(ctx, obj2, NULL);

  // release the local variables *
  sexp_gc_release2(ctx);
}

int main(int argc, char** argv) {
  sexp ctx;
  sexp_scheme_init();
  ctx = sexp_make_eval_context(NULL, NULL, NULL, 0, 0);
  sexp_load_standard_env(ctx, NULL, SEXP_SEVEN);
  sexp_load_standard_ports(ctx, NULL, stdin, stdout, stderr, 1);
  dostuff(ctx);
  sexp_destroy_context(ctx);
}
