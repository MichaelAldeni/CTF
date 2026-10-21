// solve.js - WORKING for Frida 17.9.1

var IDA_BASE    = ptr("0x555555400000");
var IDA_ADDR    = ptr("0x555555400987");
var trueOffset  = IDA_ADDR.sub(IDA_BASE);  // = 0xB95

// enumerateModules() returns a plain Array in this build
var baseAddr    = Process.enumerateModules()[0].base;
var hookAddress = baseAddr.add(trueOffset);

console.log("[*] Base:   " + baseAddr);
console.log("[*] Offset: " + trueOffset);
console.log("[*] Hook:   " + hookAddress);

// DISINNESCO DI RAND()
var randAddr = Module.getGlobalExportByName("rand");  // <-- API corretta per questa build
if (randAddr) {
    Interceptor.attach(randAddr, {
        onLeave: function(retval) {
            retval.replace(ptr(0));
        }
    });
    console.log("[+] rand() neutralizzato!");
} else {
    console.log("[-] rand() non trovata.");
}

// SPIA SUL CONTROLLO
Interceptor.attach(hookAddress, {
    onEnter: function(args) {
        var charChecked = args[0].readUtf8String(1);
        var expected1   = args[1];
        var expected2   = args[2];
        console.log("[*] char: '" + charChecked +
                    "' | p1: " + expected1 + " | p2: " + expected2);
    }
});