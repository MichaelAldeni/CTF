// debug_api.js - run BEFORE solve.js
// frida -l debug_api.js -f ./morph -- "A"

console.log("=== Frida API Debug ===");
console.log("Process keys: " + Object.keys(Process).join(", "));
console.log("");

// Test Module API
console.log("Module keys: " + Object.keys(Module).join(", "));
console.log("");

// Try every known way to get base address
try {
    var m = Process.getModuleByName("morph");
    console.log("[OK] Process.getModuleByName: " + m.base);
} catch(e) { console.log("[FAIL] Process.getModuleByName: " + e); }

try {
    var b = Module.getBaseAddress("morph");
    console.log("[OK] Module.getBaseAddress: " + b);
} catch(e) { console.log("[FAIL] Module.getBaseAddress: " + e); }

try {
    var mods = Process.enumerateModules();
    console.log("[OK] enumerateModules type: " + typeof mods);
    console.log("     constructor: " + mods.constructor.name);
    // Try array access
    try { console.log("     [0]: " + mods[0]); } catch(e2) { console.log("     [0] failed: " + e2); }
    // Try .next()
    try { console.log("     .next(): " + JSON.stringify(mods.next())); } catch(e2) { console.log("     .next() failed: " + e2); }
    // Try for..of
    try {
        var first;
        for (var x of mods) { first = x; break; }
        console.log("     for..of: " + first.base + " (" + first.name + ")");
    } catch(e2) { console.log("     for..of failed: " + e2); }
} catch(e) { console.log("[FAIL] enumerateModules: " + e); }

try {
    var mods2 = Process.enumerateModulesSync();
    console.log("[OK] enumerateModulesSync[0]: " + mods2[0].base);
} catch(e) { console.log("[FAIL] enumerateModulesSync: " + e); }

console.log("=== End Debug ===");