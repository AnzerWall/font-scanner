{
  "targets": [
    {
      "target_name": "fontmanager",
      "sources": [
        "src/FontDescriptor.cc",
        "src/FontManager.cc"
      ],
      "include_dirs": [
        "<(module_root_dir)/node_modules/node-addon-api"
      ],
      "defines": [
        "NAPI_DISABLE_CPP_EXCEPTIONS",
        "NODE_ADDON_API_ENABLE_MAYBE"
      ],
      "conditions": [
        ['OS=="mac"', {
          "sources": ["src/FontManagerMac.mm"],
          "link_settings": {
            "libraries": ["CoreText.framework", "Foundation.framework"]
          },
          "cflags+": ["-fvisibility=hidden"],
          "xcode_settings": {
            "GCC_SYMBOLS_PRIVATE_EXTERN": "YES", # -fvisibility=hidden
          }
        }],
        ['OS=="win"', {
          "sources": ["src/FontManagerWindows.cc"],
          "link_settings": {
            "libraries": ["Dwrite.lib"]
          }
        }],
        ['OS=="linux"', {
          "sources": ["src/FontManagerLinux.cc"],
          "link_settings": {
            "libraries": ["-lfontconfig"]
          }
        }]
      ]
    }
  ]
}
