let imports = {};
imports["__wbindgen_placeholder__"] = module.exports;

let cachedUint8ArrayMemory0 = null;

function getUint8ArrayMemory0() {
  if (
    cachedUint8ArrayMemory0 === null ||
    cachedUint8ArrayMemory0.byteLength === 0
  ) {
    cachedUint8ArrayMemory0 = new Uint8Array(wasm.memory.buffer);
  }
  return cachedUint8ArrayMemory0;
}

let cachedTextDecoder = new TextDecoder("utf-8", {
  ignoreBOM: true,
  fatal: true,
});

cachedTextDecoder.decode();

function decodeText(ptr, len) {
  return cachedTextDecoder.decode(
    getUint8ArrayMemory0().subarray(ptr, ptr + len),
  );
}

function getStringFromWasm0(ptr, len) {
  ptr = ptr >>> 0;
  return decodeText(ptr, len);
}

exports.say_hello = function () {
  wasm.say_hello();
};

exports.__wbg_log_6c7b5f4f00b8ce3f = function (arg0) {
  console.log(arg0);
};

exports.__wbg_wbindgenthrow_451ec1a8469d7eb6 = function (arg0, arg1) {
  throw new Error(getStringFromWasm0(arg0, arg1));
};

exports.__wbindgen_cast_2241b6af4c4b2941 = function (arg0, arg1) {
  // Cast intrinsic for `Ref(String) -> Externref`.
  const ret = getStringFromWasm0(arg0, arg1);
  return ret;
};

exports.__wbindgen_init_externref_table = function () {
  const table = wasm.__wbindgen_export_0;
  const offset = table.grow(4);
  table.set(0, undefined);
  table.set(offset + 0, undefined);
  table.set(offset + 1, null);
  table.set(offset + 2, true);
  table.set(offset + 3, false);
};

const wasmPath = `${__dirname}/hello-world.wasm`;
const wasmBytes = require("fs").readFileSync(wasmPath);
const wasmModule = new WebAssembly.Module(wasmBytes);
const wasm = (exports.__wasm = new WebAssembly.Instance(
  wasmModule,
  imports,
).exports);

wasm.__wbindgen_start();

exports.say_hello();
