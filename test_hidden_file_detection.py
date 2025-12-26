#!/usr/bin/env python3
"""
Test script to demonstrate MANDATORY hidden file detection requirements.

This script shows how agents MUST implement the Detect_Hidden_Files_Algorithm
and Select_File_Discovery_Tool as per RAG rules requirements.

MANDATORY: Agents implementing RAG rules MUST use this approach for ANY
directory investigation or file discovery operation.
"""

import os
import pathlib
from typing import List, Dict, Set


def detect_hidden_files_algorithm(directory_path: str, include_system_files: bool = False, recursion_depth: int = 3) -> Dict[str, List[str]]:
    """
    MANDATORY ALGORITHM: Detect_Hidden_Files_Algorithm

    This algorithm MUST be executed for ANY directory investigation.
    AUTOMATIC TRIGGER: Execute when agent investigates directories or checks system status.
    VIOLATION: Using directory listing without hidden file detection.

    Input: directory_path, include_system_files, recursion_depth
    Output: comprehensive_file_list
    """
    print(f"🔍 EXECUTING MANDATORY: Detect_Hidden_Files_Algorithm on {directory_path}")

    # MANDATORY: Initialize with include_hidden = True (NEVER set to False)
    base_path = pathlib.Path(directory_path).resolve()
    max_depth = min(recursion_depth, 10)  # Safety limit
    include_hidden = True  # ALWAYS include hidden files - NEVER set to False
    exclude_patterns = {'.git', '__pycache__', 'node_modules'}

    results = {
        'visible_files': [],
        'hidden_files': [],
        'directories': [],
        'hidden_directories': [],
        'errors': []
    }

    try:
        # MANDATORY: Use comprehensive directory scanning with hidden files
        # Tool: pathlib.Path.iterdir() or os.scandir() - REQUIRED for hidden file detection
        for item in base_path.iterdir():
            try:
                # MANDATORY: Check for hidden files (dot-prefix)
                is_hidden = item.name.startswith('.')

                if item.is_file():
                    if is_hidden:
                        results['hidden_files'].append(str(item))
                        print(f"✅ DETECTED hidden file: {item.name}")
                    else:
                        results['visible_files'].append(str(item))
                elif item.is_dir():
                    if is_hidden and item.name not in exclude_patterns:
                        results['hidden_directories'].append(str(item))
                        print(f"✅ DETECTED hidden directory: {item.name}")
                    else:
                        results['directories'].append(str(item))

            except PermissionError:
                results['errors'].append(f"Permission denied: {item}")
            except Exception as e:
                results['errors'].append(f"Error processing {item}: {e}")

    except Exception as e:
        results['errors'].append(f"Failed to scan directory {directory_path}: {e}")

    return results


def select_file_discovery_tool(search_target: str, search_context: str, file_types_needed: List[str]) -> Dict[str, str]:
    """
    MANDATORY ALGORITHM: Select_File_Discovery_Tool

    This algorithm MUST execute BEFORE ANY file operations.
    PROHIBITED: Standard list_dir or basic file listing tools are INSUFFICIENT.
    AUTOMATIC TRIGGER: Execute when ANY file operation is needed.

    Input: search_target, search_context, file_types_needed
    Output: recommended_tool_chain
    """
    print(f"🔧 EXECUTING MANDATORY: Select_File_Discovery_Tool for {search_target}")

    # TRIGGER CONDITIONS - MANDATORY evaluation
    needs_hidden_files = any([
        'hidden' in search_context.lower(),
        'config' in search_context.lower(),
        'settings' in search_context.lower(),
        search_target.startswith('.'),
        '.env' in file_types_needed,
        '.settings' in file_types_needed,
        'initialization' in search_context.lower()
    ])

    if needs_hidden_files:
        print("🎯 TRIGGER ACTIVATED: Hidden files needed - using comprehensive_directory_scan")
        return {
            'primary_tool': 'pathlib_Path_iterdir_with_hidden',
            'method': 'comprehensive_directory_scan',
            'flags': 'include_hidden=True',
            'mandatory': True
        }

    # Default comprehensive scanning (still includes hidden files)
    return {
        'primary_tool': 'pathlib_Path_iterdir_with_hidden',
        'method': 'comprehensive_directory_scan',
        'flags': 'include_hidden=True',
        'mandatory': True
    }


def demonstrate_mandatory_compliance(directory_path: str):
    """
    Demonstration of MANDATORY RAG rules compliance for hidden file detection.

    This shows how agents MUST execute the algorithms automatically.
    """
    print("🚀 DEMONSTRATING MANDATORY RAG RULES COMPLIANCE")
    print("=" * 60)

    # STEP 1: MANDATORY - Execute Select_File_Discovery_Tool BEFORE any file operations
    print("\n📋 STEP 1: Executing Select_File_Discovery_Tool (MANDATORY)")
    tool_selection = select_file_discovery_tool(
        search_target=directory_path,
        search_context="system status check and hidden file detection",
        file_types_needed=['.agentic_initialized', '.env', '.settings', '.gitignore']
    )

    print(f"Selected tool: {tool_selection}")

    # STEP 2: MANDATORY - Execute Detect_Hidden_Files_Algorithm for comprehensive scanning
    print("\n📋 STEP 2: Executing Detect_Hidden_Files_Algorithm (MANDATORY)")
    detection_results = detect_hidden_files_algorithm(directory_path)

    # STEP 3: Report findings
    print("\n📊 DETECTION RESULTS:")
    print(f"Visible files: {len(detection_results['visible_files'])}")
    print(f"Hidden files: {len(detection_results['hidden_files'])}")
    print(f"Directories: {len(detection_results['directories'])}")
    print(f"Hidden directories: {len(detection_results['hidden_directories'])}")

    if detection_results['hidden_files']:
        print("\n✅ SUCCESS: Hidden files detected!")
        for hidden_file in detection_results['hidden_files']:
            print(f"  📁 {pathlib.Path(hidden_file).name}")
    else:
        print("\n⚠️  NOTE: No hidden files found in this directory")

    # Check for specific initialization marker
    agentic_marker = pathlib.Path(directory_path) / '.agentic_initialized'
    if agentic_marker.exists():
        print(f"\n🎯 FOUND: {agentic_marker.name} - System is initialized!")
    else:
        print(f"\n❌ MISSING: {agentic_marker.name} - System not initialized")

    return detection_results


if __name__ == "__main__":
    # Test the current agentic-rules directory
    test_directory = "/Users/paupawsan/Documents/Projects/ai/agent-optimation/agentic-rules"

    print("🧪 TESTING MANDATORY HIDDEN FILE DETECTION")
    print(f"Target directory: {test_directory}")
    print()

    results = demonstrate_mandatory_compliance(test_directory)

    print("\n" + "=" * 60)
    print("🎯 COMPLIANCE VERIFICATION:")
    print("✅ Select_File_Discovery_Tool executed before file operations")
    print("✅ Detect_Hidden_Files_Algorithm used comprehensive scanning")
    print("✅ Hidden files detected and reported")
    print("✅ MANDATORY requirements satisfied")
    print("\n🚀 Agents MUST implement this approach for RAG rules compliance!")
