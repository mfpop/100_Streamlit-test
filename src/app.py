import streamlit as st
import st_tailwind as tw

st.set_page_config("Streamlit Tailwind Examples")
tw.initialize_tailwind()


def main():
    tw.initialize_tailwind()

    with st.sidebar:
        tw.write("Sidebar Title", classes="text-2xl font-bold text-blue-500")
        tw.button("Home", classes="bg-blue-500 text-white w-full py-2 my-2")
        tw.button("About", classes="bg-green-500 text-white w-full py-2 my-2")
        tw.button("Contact", classes="bg-red-500 text-white w-full py-2 my-2")

    tw.write("Grid Container", classes="text-blue-500 pb-4")

    with tw.container(classes="grid grid-cols-4"):
        for idx in range(1, 25):
            st.button(f"Button {idx}")
    tw.write("Colored Button", classes="text-purple-700 pb-4")
    tw.button("Button", classes="bg-red-500")


if __name__ == "__main__":
    main()
