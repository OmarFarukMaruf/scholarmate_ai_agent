import asyncio
from google.genai.types import Content, Part

from scholarmate_agent.app import create_runner
from scholarmate_agent.config.settings import APP_NAME, USER_ID_NAMESPACE

async def chat_loop():
    runner = create_runner()
    session_id = "local_demo_student"

    print("Scholarship Finder Agent (local). Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in {"exit", "quit"}:
            break

        user_content = Content(
            role="user",
            parts=[Part(text=user_input)]
        )

        final_text = "(no response)"

        async for event in runner.run_async(
            app_name=APP_NAME,
            user_id=USER_ID_NAMESPACE,
            session_id=session_id,
            new_message=user_content,
        ):
            if event.is_final_response() and event.content and event.content.parts:
                final_text = event.content.parts[0].text

        # After each turn, add session to memory:
        session = await runner.session_service.get_session(
            app_name=APP_NAME,
            user_id=USER_ID_NAMESPACE,
            session_id=session_id,
        )
        await runner.memory_service.add_session_to_memory(session)

        print(f"\nAgent:\n{final_text}\n")

def main():
    asyncio.run(chat_loop())

if __name__ == "__main__":
    main()