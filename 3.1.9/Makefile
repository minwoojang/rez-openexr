SHELL := /bin/bash

# Rez variables, setting these to sensible values if we are not building from rez
REZ_BUILD_PROJECT_VERSION ?= NOT_SET
REZ_BUILD_INSTALL_PATH ?= $(REZ_BUILD_INSTALL_PATH)#/home/minwoo/packages/openexr/3.0.2/platform-linux/arch-x86_64
REZ_BUILD_SOURCE_PATH ?= $(shell dirname $(lastword $(abspath $(MAKEFILE_LIST))))
BUILD_ROOT := $(REZ_BUILD_SOURCE_PATH)/build
REZ_BUILD_PATH ?= $(BUILD_ROOT)

# Direct paths for Rez packages
REZ_LIBPNG_PATH := /cocoa/inhouse/tool/rez-packages/png/1.6.29/platform-linux/arch-x86_64
REZ_ZLIB_PATH := /cocoa/inhouse/tool/rez-packages/zlib/1.3.1/platform-linux/arch-x86_64

# Build time locations
SOURCE_DIR := $(BUILD_ROOT)/openexr
BUILD_TYPE = Release
BUILD_DIR = ${REZ_BUILD_PATH}/BUILD/$(BUILD_TYPE)

# Source
REPOSITORY_URL := https://github.com/AcademySoftwareFoundation/openexr.git
TAG ?= v$(REZ_BUILD_PROJECT_VERSION)

# Installation prefix (modified to the desired path)
# PREFIX ?= /home/minwoo/packages/openexr/3.0.2/platform-linux/arch-x86_64

$(info $(REZ_BUILD_INSTALL_PATH))

# CMake Arguments (Add the paths to libpng and zlib here)
CMAKE_ARGS := -DCMAKE_INSTALL_PREFIX=$(REZ_BUILD_INSTALL_PATH) \
    -DCMAKE_BUILD_TYPE=$(BUILD_TYPE) \
    -DCMAKE_SKIP_RPATH=ON \
    -DCMAKE_CXX_STANDARD=17 \
    -DOPENEXR_BUILD_PYTHON=OFF \
    -DCMAKE_PREFIX_PATH=$(REZ_LIBPNG_PATH):$(REZ_ZLIB_PATH)

# Warn about building master if no tag is provided
ifeq "$(TAG)" "vNOT_SET"
    $(warning "No tag was specified, main will be built. You can specify a tag: TAG=v2.1.0")
    TAG:=master
endif

.PHONY: build install test clean
.DEFAULT: build

# Prepare build directories
$(BUILD_DIR): 
	# Ensure tabs, not spaces, are used before commands
	mkdir -p $(BUILD_ROOT)
	mkdir -p $(BUILD_DIR)

# Clone the repository if the source directory does not exist
$(SOURCE_DIR): | $(BUILD_DIR) 
	# Ensure tabs, not spaces, are used before commands
	@if [ ! -d "$(SOURCE_DIR)" ]; then \
		cd $(BUILD_ROOT) && git clone $(REPOSITORY_URL); \
	fi

# Checkout the correct tag and build
# 
build: $(SOURCE_DIR)
	# Ensure tabs, not spaces, are used before commands
	cd $(SOURCE_DIR) && git fetch --all && git checkout $(TAG)
	cd $(BUILD_DIR) && cmake $(CMAKE_ARGS) \
		-DCMAKE_RUNTIME_OUTPUT_DIRECTORY=$(BUILD_DIR)/bin \
		$(SOURCE_DIR) && make

# Install the built files
install: build
	# Ensure tabs, not spaces, are used before commands
	# mkdir -p $(REZ_BUILD_INSTALL_PATH)
	cd $(BUILD_DIR) && make install

	# Copy the built binaries to the specified install directory
	mkdir -p $(REZ_BUILD_INSTALL_PATH)/bin/
	cp $(BUILD_DIR)/bin/* $(REZ_BUILD_INSTALL_PATH)/bin/
	

	# Copy the shared libraries to lib64
	# cp $(BUILD_DIR)/src/lib/Iex/libIex-3_1.so $(REZ_BUILD_INSTALL_PATH)/lib64/
	# cp $(BUILD_DIR)/src/lib/IlmThread/libIlmThread-3_1.so $(REZ_BUILD_INSTALL_PATH)/lib64/
	# cp $(BUILD_DIR)/src/lib/OpenEXR/libOpenEXR-3_1.so $(REZ_BUILD_INSTALL_PATH)/lib64/
	# cp $(BUILD_DIR)/src/lib/OpenEXRUtil/libOpenEXRUtil-3_0.so $(REZ_BUILD_INSTALL_PATH)/lib64/

	# Create symbolic links for compatibility
	#$(REZ_BUILD_INSTALL_PATH)/lib64/
	
	# ln -sf libIex-3_1.so $(REZ_BUILD_INSTALL_PATH)/lib64/libIex-3_0.so
	# ln -sf libIex-3_1.so $(REZ_BUILD_INSTALL_PATH)/lib64/libIex-3_0.so.28
	# ln -sf libIlmThread-3_1.so $(REZ_BUILD_INSTALL_PATH)/lib64/libIlmThread-3_0.so
	# ln -sf libIlmThread-3_1.so $(REZ_BUILD_INSTALL_PATH)/lib64/libIlmThread-3_0.so.28
	# ln -sf libOpenEXR-3_1.so $(REZ_BUILD_INSTALL_PATH)/lib64/libOpenEXR-3_0.so
	# ln -sf libOpenEXR-3_1.so $(REZ_BUILD_INSTALL_PATH)/lib64/libOpenEXR-3_0.so.28
	# ln -sf libOpenEXRUtil-3_1.so $(REZ_BUILD_INSTALL_PATH)/lib64/libOpenEXRUtil-3_0.so
	# ln -sf libOpenEXRUtil-3_1.so $(REZ_BUILD_INSTALL_PATH)/lib64/libOpenEXRUtil-3_0.so.28

# Run the tests in the build
test: build
	# Ensure tabs, not spaces, are used before commands
	$(MAKE) -C $(BUILD_DIR) test

# Clean the build directory
clean:
	# Ensure tabs, not spaces, are used before commands
	rm -rf $(BUILD_ROOT)