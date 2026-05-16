import streamlit as st
import subprocess
import os


st.set_page_config(page_title="AI QA Dashboard", layout="wide")

st.title("AI-Powered Agentic Automation Framework")

st.markdown(
    """
    Run Selenium + Pytest AI Automation Tests

    Features:
    - AI Self-Healing
    - Retry Engine
    - Failure Analysis
    - Intelligent Recovery
    """
)

# Test File Input
test_name = st.text_input("Enter Test File Name", placeholder="test_ai_failure.py")

# Run Button
run_btn = st.button("Run Test")

# Execute Test
if run_btn:
    if test_name.strip():
        with st.spinner("Running AI Automation Test..."):
            result = subprocess.run(
                ["pytest", f"tests/{test_name}", "-s", "--log-cli-level=INFO"],
                capture_output=True,
                text=True,
            )

            logs = result.stdout

            # FULL EXECUTION LOGS
            st.subheader("Execution Logs")

            st.code(logs)

            # PASS / FAIL STATUS
            if "PASSED" in logs:
                st.success("Test Passed Successfully")

            elif "FAILED" in logs:
                st.error("Test Failed")

            # AI SELF HEALING SECTION
            if "LLM Locator Suggestions" in logs:
                st.subheader("AI Self-Healing Suggestions")

                start = logs.find("LLM Locator Suggestions")

                end = logs.find("Recovered using AI locator")

                if end == -1:
                    end = start + 1000

                healing_logs = logs[start:end]

                st.success(healing_logs)

            # AI FAILURE ANALYSIS
            if "LLM Analysis" in logs:
                st.subheader("AI Failure Analysis")

                start = logs.find("LLM Analysis")

                end = start + 3000

                failure_analysis = logs[start:end]

                st.error(failure_analysis)

            # RETRY LOGS
            if "Retry Attempt" in logs:
                st.subheader("Retry Engine Logs")

                retry_logs = []

                for line in logs.splitlines():
                    if "Retry Attempt" in line:
                        retry_logs.append(line)

                st.warning("\n".join(retry_logs))

            # SCREENSHOT DISPLAY
            screenshot_folder = "screenshots"

            if os.path.exists(screenshot_folder):
                screenshots = os.listdir(screenshot_folder)

                if screenshots:
                    latest_screenshot = sorted(screenshots)[-1]

                    screenshot_path = os.path.join(screenshot_folder, latest_screenshot)

                    st.subheader("Execution Screenshot")

                    st.image(screenshot_path, caption=latest_screenshot)

    else:
        st.warning("Please enter test file name")
